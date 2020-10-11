from typing import List
from utils import key_exists
from constants import ENABLE, USERNAMES, AMOUNT, RANDOMIZE, INTERACT, SLEEP_DELAY
import sys


class Follow:
    __enable: bool = True
    __usernames: List[str] = []
    __amount: int = 250
    __randomize: bool = True
    __interact: bool = False
    __sleep_delay: int = 600

    def __init__(self, follow_config):
        if follow_config:
            if key_exists(ENABLE, follow_config):
                self.__set_enable(follow_config[ENABLE])

            if key_exists(USERNAMES, follow_config):
                self.__set_usernames(follow_config[USERNAMES])

            if key_exists(AMOUNT, follow_config):
                self.__set_amount(follow_config[AMOUNT])

            if key_exists(RANDOMIZE, follow_config):
                self.__set_randomize(follow_config[RANDOMIZE])

            if key_exists(INTERACT, follow_config):
                self.__set_interact(follow_config[INTERACT])

            if key_exists(SLEEP_DELAY, follow_config):
                self.__set_sleep_delay(follow_config[SLEEP_DELAY])

            if self.__enable and len(self.__usernames) == 0:
                sys.exit('[ERROR]: Please provide usernames to follow')

    def get_enable(self) -> bool:
        return self.__enable

    def get_usernames(self) -> List[str]:
        return self.__usernames

    def get_amount(self) -> int:
        return self.__amount

    def get_randomize(self) -> bool:
        return self.__randomize

    def get_interact(self) -> bool:
        return self.__interact

    def get_sleep_delay(self) -> int:
        return self.__sleep_delay

    def __set_enable(self, enable: bool):
        if type(enable) is not bool:
            sys.exit('[ERROR]: follow.enable should be a boolean type.')
        self.__enable = enable

    def __set_interact(self, interact: bool):
        if type(interact) is not bool:
            sys.exit('[ERROR]: follow.interact should be a boolean type.')
        self.__interact = interact

    def __set_usernames(self, usernames: List[str]):
        if type(usernames) is not list:
            sys.exit('[ERROR]: follow.usernames should be an array of string.')
        self.__usernames = usernames

    def __set_amount(self, amount: int):
        if type(amount) is not int:
            sys.exit('[ERROR]: follow.amount should be an int type.')
        self.__amount = amount

    def __set_randomize(self, randomize: int):
        if type(randomize) is not int:
            sys.exit('[ERROR]: follow.randomize should be an int type.')
        self.__randomize = randomize

    def __set_sleep_delay(self, sleep_delay: int):
        if type(sleep_delay) is not int:
            sys.exit('[ERROR]: follow.sleep_delay should be an int type.')
        self.__sleep_delay = sleep_delay
