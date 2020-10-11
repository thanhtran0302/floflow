from typing import List
from utils import key_not_exists, key_exists
from follow import Follow
from constants import USERNAME, PASSWORD, FOLLOW

import sys


class Account:
    __username: str = None
    __password: str = None
    __follow: Follow = None

    def __init__(self, config):
        if key_not_exists(USERNAME, config):
            sys.exit('[ERROR]: No username provided')
        elif key_not_exists(PASSWORD, config):
            sys.exit('[ERROR]: No password provided')

        self.__username = config[USERNAME]
        self.__password = config[PASSWORD]

        if key_exists(FOLLOW, config):
            self.__follow = Follow(config[FOLLOW])

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_follow(self):
        return self.__follow
