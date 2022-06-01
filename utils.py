import requests
import logging
from logging import Logger

CONFIG_JSON_URL = "http://{}:{}/public/default/config.json"
DEFAULT_WEBSOCKET_PORT = 8765
DEFAULT_HTTP_PORT = 8766

def getHttpPort(ip: str, room_port: int, logger: Logger) -> int:
    """Get the current HTTP TrueConf Room or VideoSDK port. The TrueConf Room or VideoSDK application must be launched"""
    try:
        json_file = requests.get(url=CONFIG_JSON_URL.format(ip, room_port))
        data = json_file.json()
        port = data["config"]["http"]["port"]
        #logger.info(f'HTTP port: {port}')
    except Exception as e:
        port = DEFAULT_HTTP_PORT
        #logger.warning(f'Failed to fetch HTTP port: {e}')
        #logger.warning(f'Set HTTP port to default: {port}')

    return port


def getWebsocketPort(ip: str, room_port: int, logger: Logger) -> int:
    """Get the current websocket TrueConf Room or VideoSDK port. The TrueConf Room or VideoSDK application must be launched"""
    try:
        json_file = requests.get(url=CONFIG_JSON_URL.format(ip, room_port))
        data = json_file.json()
        port = data["config"]["websocket"]["port"]
        #logger.info(f'WebSocket port: {port}')
    except Exception as e:
        port = DEFAULT_WEBSOCKET_PORT
        #logger.warning(f'Failed to fetch current websocket port: {e}')
        #logger.warning(f'Set WebSocket port to default: {port}')

    return port