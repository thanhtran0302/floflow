from typing import List
from utils import key_checker
from follow import Follow

import sys


class Account:
    __username: str = None
    __password: str = None
    __follow: Follow = None

    def __init__(self, config):
        if key_checker('username', config):
            sys.exit('[ERROR]: No username provided')
        elif key_checker('password', config):
            sys.exit('[ERROR]: No password provided')

        self.__username = config['username']
        self.__password = config['password']

        if not key_checker('follow', config):
            self.__follow = Follow(config['follow'])

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_follow(self):
        return self.__follow
