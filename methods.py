import pyVideoSDK

class Methods:
    def __init__(self, videosdk: pyVideoSDK.VideoSDK):
        self.videosdk = videosdk

    def __del__(self):
        pass

    def call(self, peerId: str) -> None:
        """Make p2p call
        
        Parameters
        ----------
        peerId : str
            A unique user ID (TrueConfID)
        """
        command = {"method": "call", "peerId": peerId}
        self.videosdk.command(command)

    def accept(self):
        """Accept the call. The command is run immediately and the result of execution is received at once.
        
        Response example
        ----------
        {"event" : "commandExecution", "accept" : "ok"}

        """
        command = {"method": "accept"}
        self.videosdk.command(command)

    def hangUp(self, forAll: bool = False):
        """End a call or a conference. The command is used when the conference has already been created. 
        hangUp() format is used during a video call. During group conferences both formats are used. 
        By using hangUp(False) format, you leave the conference, but other participants remain in the conference. 
        By using hangUp(True) the conference ends for all the participants. 
        hangUp(True) is used only if you are the conference owner, otherwise a failure occurs. 
        Positive response ("ok") means the command has been accepted for execution but has not been run executed yet. 
        Execution result will be received separately via notification.
        
        Parameters
        ----------
            forAll: bool
                True - conference ends for all the participants;                 
                False - you leave the conference, but other participants remain in the conference.
        """
        command = {"method": "hangUp", "forAll": forAll}
        self.videosdk.command(command)

    def login(self, callId: str, password: str):
        """Login to TrueConf Server"""
        command = {"method" : "login",
            "login" : callId,
            "password" : password,
            "encryptPassword" : True}
        self.videosdk.command(command)

    def logout(self):
        """Log out the current user"""
        command = {"method": "logout"}
        self.videosdk.command(command)

    def connectToServer(self, server: str, port: int = 4307):
        """Connect to TrueConf Server
        
        Parameters
        ----------
            server: str
                Server address. For example, IP address;
            port: int
                Port. Default port is 4307.
        """
        command = {"method": "connectToServer", "server": server, "port": port}
        self.videosdk.command(command)

    def sendCommand(self, peerId: str, command: str):
        command = {"method": "sendCommand", "peerId": peerId, "command": command}
        self.videosdk.command(command)

    def showMainWindow(self, maximized: bool, stayOnTop: bool = True):
        # state:
        #   1 = minimized;
        #   2 = full screen mode.        
        state = 1 if not maximized else 2
        command = {"method": "changeWindowState", "windowState": state, "stayOnTop": stayOnTop}
        self.videosdk.command(command)

    def reject(self):
        '''
        The command allows to reject incoming call or invitation to the conference
        '''
        command = {"method": "reject"}
        self.videosdk.command(command)

    def rejectPeer(self, peerId: str):
        '''
        Reject user’s request to join your conference

        Parameters:

            peerId: str 
                unique user ID
        '''
        command = {"method": "rejectPeer", "peerId": peerId}
        self.videosdk.command(command)

    def acceptPeer(self, peerId: str):
        '''
        Accept a request from the user to participate in your conference

        Parameters:

            peerId: str 
                unique user ID
        '''
        command = {"method": "acceptPeer", "peerId": peerId}
        self.videosdk.command(command)