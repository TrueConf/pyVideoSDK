# coding=utf8
'''''
@author: zobov
'''
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import logging
import requests
from threading import Lock, Thread
from logging.handlers import RotatingFileHandler
from logging import Formatter
from enum import Enum, IntEnum
import pyVideoSDK.utils

__status__  = "Development"
__authors__ = ["Andrey Zobov", "Pavel Titov"]
__contact__ = "azobov@trueconf.com"
__deprecated__ = False
__email__ =  "azobov@trueconf.com"
__version__ = "0.1"
__date__    = "12 May 2022"

# PORTS: c:\ProgramData\TrueConf\VideoSDK\web\default\config.json
# CONFIG_JSON_FILE = "c:\ProgramData\TrueConf\VideoSDK\web\default\config.json"

PRODUCT_NAME = 'TrueConf VideoSDK'

DEFAULT_ROOM_PORT = 80
QUEUE_INTERVAL = 0.05

logger = logging.getLogger('tcroom')
logger.setLevel(logging.DEBUG)

rotation_handler = logging.handlers.RotatingFileHandler(
    filename='tcroom.log',
    maxBytes=1024 ** 2 * 10,  # 10 MB
    backupCount=3
)
rotation_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))

console_handler = logging.StreamHandler()
console_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(rotation_handler)
logger.addHandler(console_handler)


class SessionStatus(IntEnum):
    unknown = 0
    started = 1
    connected = 2
    normal = 3
    close = 4

APPLICATION_STATE = {
    0: {"name": "none",       "hint": f'No connection to the server and {PRODUCT_NAME} does nothing'},
    1: {"name": "connect",    "hint": f'{PRODUCT_NAME} tries to connect to the server'},
    2: {"name": "login",      "hint": f'{PRODUCT_NAME} need to login'},
    3: {"name": "normal",     "hint": f'{PRODUCT_NAME} is connected to the server and logged in'},
    4: {"name": "wait",       "hint": f'{PRODUCT_NAME} is pending: either it calls somebody or somebody calls it'},
    5: {"name": "conference", "hint": f'{PRODUCT_NAME} is in the conference'},
    6: {"name": "close",      "hint": f'{PRODUCT_NAME} is finishing the conference'}
}

class CustomSDKException(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)


class ConnectToSDKException(CustomSDKException):
    pass


def check_schema(schema: dict, data: dict, exclude_from_comparison: list = []) -> bool:
    schema_d = {k: v for k, v in data.items() if k in schema.keys()}
    if len(schema) == len(schema_d):
        # Exclude some values from comparison
        #  all "key": None
        exclude = [k for k, v in schema.items() if v is None]
        #  and all specified
        exclude.extend(exclude_from_comparison)
        # Comparison        
        for k in schema:
            if k not in exclude:
                try:
                    if schema[k].lower() != schema_d[k].lower():
                        return False
                except:
                    return False
    else:
        return False

    return True


class VideoSDK:
    def __init__(self, debug):
        self.debug = debug
        self.lock = Lock()
        self.session_status = SessionStatus.unknown
        self.app_state = 0
        self.app_state_list = []
        self.ip = ''
        self.pin = ''
        self.url = ''
        self.auth_token = ''
        self.http_port = None

        self.systemInfo = {}
        self.settings = {}
        self.monitors_info = {}

        self.websocket = None
        self.current_conference = None

        self.api_handlers = []
        self.command_queue = []
        self.thread_queue = Thread(target = self.__process_queue, daemon = True)
        self.thread_queue.start()

    def __del__(self):
        pass

    def __add_handler__(self, handle: dict, function: object):
        self.api_handlers.append([handle, function])

    # Send directly to websocket
    def __send_to_websocket(self, command: dict):
        self.websocket.send(json.dumps(command))

    def __process_queue(self):
        while True:
            self.lock.acquire()
            try:
                if len(self.command_queue) > 0 & self.isConnected():
                    # Extract a first from the queue
                    command = self.command_queue.pop(0)
                    # Send it to websocket
                    self.__send_to_websocket(command)
            finally:
                self.lock.release()
            # Waiting...
            time.sleep(QUEUE_INTERVAL)

    # ===================================================
    # Processing of the all incoming
    # ===================================================
    def __process_message(self, msg: str):
        response = json.loads(msg)
        self.__process_app_state(response)
        self.__process_auth(response)
        self.__process_error(response)
        self.__process_method(response)

        for item in self.api_handlers:
            if check_schema(item[0], response):
                func_handler = item[1]
                # Call the Handler function
                func_handler(response)

    # 1) Event: appStateChanged
    # 2) Request for getAppState
    def __process_app_state(self, response) -> bool:
        
        def add_state_to_list(state: int):
            self.app_state_list.insert(0, state)
            if len(self.app_state_list) > 10:
                self.app_state_list = self.app_state_list[0:10]

        # New status event
        if check_schema({"event": "appStateChanged", "appState": None}, response):
            new_state = response["appState"]
            self.app_state = new_state
            # queue
            add_state_to_list(self.app_state)
            # update a conference's info
            self.__update_conference_info()
            # To log
            logger.info(f'Application state is {self.app_state}: {APPLICATION_STATE[self.app_state]["hint"]}')
        # Response
        elif check_schema({"appState": None, "method": "getAppState", "result": None}, response):
            new_state = response["appState"]
            self.app_state = new_state
            # update a conference's info
            self.__update_conference_info()
            # To log
            logger.info(f'Application state is {self.app_state}: {APPLICATION_STATE[self.app_state]["hint"]}')     

    # {"requestId":"","method":"auth","previleges":2,"token":"***","tokenForHttpServer":"***","result":true}
    def __process_auth(self, response) -> bool:
        # CHECK SCHEMA
        if check_schema({"method": "auth", "result": None}, response):
            if response["result"]:
                self.auth_token = response["tokenForHttpServer"]
                self.__set_session_status(SessionStatus.normal)
                # requests Info
                self.__request_info()
            else:
                logger.error(f'Auth error: {response}')
                self.close_session()
                self.caughtConnectionError()  # any connection errors

    def __process_error(self, response) -> bool:
        # CHECK SCHEMA
        if check_schema({"error": None}, response):
            s = f'VideoSDK error: {response["error"]}'
            logger.warning(s)

    def __process_method(self, response) -> bool:
        result = check_schema({"method": None}, response) and not check_schema({"event": None}, response)
        if result:
            method_name = response["method"]
            # Info
            if "getSystemInfo".lower() == method_name.lower():
                self.systemInfo = response
            elif "getSettings".lower() == method_name.lower():
                self.settings = response
            elif "getMonitorsInfo".lower() == method_name.lower():
                self.monitors_info = response
            elif "getConferences".lower() == method_name.lower():
                self.current_conference = response

    # =======================================
    # WebSocket's callback functions
    # =======================================
    def __WS_message(self, ws, message):
        try:
            self.__process_message(message)
        except Exception as e:
            logger.error(f'Socket data processing error. {e.__class__}: {str(e)}')

    def __WS_error(self, ws, error):
        logger.error(f'WebSocket connection error: {error}')

    def __WS_close(self, ws, *args):
        self.__set_session_status(SessionStatus.close)
        self.auth_token = ""

    def __WS_open(self, ws):
        logger.info(f'{PRODUCT_NAME} connection to {self.url} open successfully')
        self.__set_session_status(SessionStatus.connected)
        time.sleep(0.1)
        self.__auth(self.pin)

        def run(*args):
            while self.isConnected():
                time.sleep(0.1)
            self.websocket.close()

        #thread.start_new_thread(run, ())
    # =======================================

    def __run_socket(self):
        self.websocket.run_forever()

    def __set_session_status(self, status):
        self.session_status = status
        logger.info(f'Session status: {self.session_status.name}')

    def __auth(self, pin: str):
        if pin:
            command = {"method": "auth", "type": "secured", "credentials": pin}
        else:
            command = {"method": "auth", "type": "unsecured"}
        self.__send_to_websocket(command)

    def __request_info(self):
        # Request an application state
        command = {"method": "getAppState"}
        self.__send_to_websocket(command)
        # Request the settings list
        command = {"method": "getSettings"}
        self.__send_to_websocket(command)
        # Request the system information
        command = {"method": "getSystemInfo"}
        self.__send_to_websocket(command)
        # Request the information about monitors.
        command = {"method": "getMonitorsInfo"}
        self.__send_to_websocket(command)
        
    def __update_conference_info(self):
        # clear current conference info
        self.current_conference = None
        # update info
        if self.app_state == 5:
            self.__get_conferences()

    def __get_conferences(self):
        """Request the list of conferences."""
        command = {"method": "getConferences"}
        self.__send_to_websocket(command)

    # =====================================================
    # Public exception
    # =====================================================
    def caughtConnectionError(self, text = None):
        if text:
            raise ConnectToSDKException(text)
        else:
            raise ConnectToSDKException(
                f'{PRODUCT_NAME} is not running or wrong IP address, PIN, Port: IP = "{self.ip}", PIN = "{self.pin}", Port = {self.port}')

    # =====================================================
    # Public functions
    # =====================================================
    def handler(self, filter: dict):
        """
        A decorator that is used to register a handler function for a giver filter

        Parameters:

        filter: dict
            Filer

        Example::

            room = pyVideoSDK.open_session(ip = "127.0.0.1", port = 80, pin = "123", debug = True)

            @room.handler({"event":  "appStateChanged", "appState": None})
            @room.handler({"method": "getAppState", "appState": None, "result": None})
            def on_state_change(response):
                print(f'AppState = {response["appState"]}')

        """
        logger.info(f'Add processing handler: {filter}')
        def decorator(f):
            self.__add_handler__(filter, f)
            return f

        return decorator

    def add_handler(self, filter: dict, method: object):
        """
        Register a class member method as an event handler

        Parameters:

            filter: dict
                Filter

            method: object
                Class member function
        """
        self.__add_handler__(filter, method)
    
    def del_handler(self, method: object):
        """
        Unregister handler

        Parameters:

            method: object
                The previous registered class member function
        """
        i = 0
        while i < len(self.api_handlers):
            if self.api_handlers[i][1] == method:
                self.api_handlers.pop(i)
            else:
                i += 1

    # Add new command to queue
    def command(self, command: dict):
        """
        Send a command through WebSocket

        Parameters:

        command : dict
            The command

        Example::

            command({"method": "call", "peerId": "user1@some.server"})

        """
        self.lock.acquire()
        try:
            self.command_queue.append(command)
        finally:
            self.lock.release()

    def run(self):
        print("\nPress Ctrl+c for exit.\n")
        try:
            while True:
                if not self.isConnected():
                    break

                time.sleep(0.2)
        except KeyboardInterrupt:
            print('Exit by Ctrl + c')
        except CustomSDKException as e:
            print('VideoSDK error: {e}')

    def open_session(self, ip: str, port: int, pin: str = None) -> bool:
        """
        Create new session

        Parameters:

        ip: str 
            IP address
        port: int
            Port
        pin: str
            Authentication string

        Example::

            open_session(ip="127.0.0.1", port="80", pin="PIN123")

        """
        self.ip = ip
        self.port = port
        self.pin = pin
        self.in_stopping = False
        self.auth_token = ""

        self.wsPort = utils.getWebsocketPort(ip, port, logger)
        self.http_port = utils.getHttpPort(ip, port, logger)
        
        websocket.enableTrace(self.debug)
        self.url = f'ws://{self.ip}:{self.wsPort}'
        self.websocket = websocket.WebSocketApp(self.url,
                                                 on_open=self.__WS_open,
                                                 on_message=self.__WS_message,
                                                 on_error=self.__WS_error,
                                                 on_close=self.__WS_close)
        #self.connection.on_open = self.on_open
        self.__set_session_status(SessionStatus.started)
        thread.start_new_thread(self.__run_socket, ())

    def close_session(self):
        """Disconnect from the VideoSDK application"""
        logger.info('Connection is closing...')
        self.__set_session_status(SessionStatus.close)

    def getAppState(self) -> int:
        ''' 
        * none       = 0 (No connection to the server and the terminal does nothing),
        * connect    = 1 (the terminal tries to connect to the server),
        * login      = 2 (you need to login),
        * normal     = 3 (the terminal is connected to the server and logged in),
        * wait       = 4 (the terminal is pending: either it calls somebody or somebody calls it),
        * conference = 5 (the terminal is in the conference),
        * close      = 6 (the terminal is finishing the conference)
        '''
        return self.app_state

    def TrueConfID(self) -> str:
        """
        Get the current logged TrueConf ID
        """

        try:
            return self.systemInfo["authInfo"]["peerId"]
        except:
            return None

    def getTokenForHttpServer(self):
        return self.auth_token

    def isReady(self):
        return self.session_status == SessionStatus.normal

    def isConnected(self) -> bool:
        return self.session_status in [SessionStatus.connected, SessionStatus.normal]
    
    def getSelfViewURL(self) -> str:
        return f'http://{self.ip}:{self.http_port}/frames/?peerId=%23self%3A0&token={self.auth_token}'

# ========================================================================================
def open_session(ip: str, port: int = 80, pin: str = None, debug: bool = False): 
    """
    Create a new object instance and open a session.

    Parameters:

    ip: str 
        IP address
    port: int
        Port
    pin: str
        Authentication string
    debug: bool
        Write more debug information to the console and to the log-file

    Example::

        room = pyVideoSDK.open_session(ip="127.0.0.1", port="80", pin="PIN123", debug = True)

    """

    room = VideoSDK(debug)
    room.open_session(ip=ip, pin=pin, port=port)

    # Wait for ~5 sec...
    WAIT_FOR_SEC, SLEEP = 5, 0.1
    for i in range(round(WAIT_FOR_SEC / SLEEP)):
        if room.isConnected():
            break
        time.sleep(0.1)
        if i >= round(WAIT_FOR_SEC / SLEEP) - 1:
            logger.error('Connection timed out')
            room.caughtConnectionError('Connection timed out')

    return room