from utils import key_not_exists
from constants import USERNAME, PASSWORD

import sys


class Account:
    __username: str = None
    __password: str = None

    def __init__(self, config: object):
        if key_not_exists(USERNAME, config):
            sys.exit('[ERROR]: No username provided')
        elif key_not_exists(PASSWORD, config):
            sys.exit('[ERROR]: No password provided')

        self.__set_username(config[USERNAME])
        self.__set_password(config[PASSWORD])

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def __set_username(self, username: str) -> None:
        if type(username) is not str:
            sys.exit('[ERROR]: username should be a string type.')
        self.__username = username

    def __set_password(self, password: str) -> None:
        if type(password) is not str:
            sys.exit('[ERROR]: password should be a string type.')
        self.__password = password
