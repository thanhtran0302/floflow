import sys
from constants import ENABLE, USERNAMES, AMOUNT, RANDOMIZE, INTERACT, \
    SLEEP_DELAY, FOLLOW, BY_TAGS
from typing import List
from utils import key_exists, key_not_exists
from follow_by_tags import FollowByTags


class Follow:
    __enable: bool = False
    __usernames: List[str] = []
    __amount: int = 250
    __randomize: bool = True
    __interact: bool = False
    __sleep_delay: int = 600
    __session = None
    __by_tags: FollowByTags = None

    def __init__(self, config: object, session):
        if key_exists(FOLLOW, config):
            follow = config[FOLLOW]
            if key_exists(ENABLE, follow):
                self.__set_enable(follow[ENABLE])

            if key_exists(USERNAMES, follow):
                self.__set_usernames(follow[USERNAMES])

            if key_exists(AMOUNT, follow):
                self.__set_amount(follow[AMOUNT])

            if key_exists(RANDOMIZE, follow):
                self.__set_randomize(follow[RANDOMIZE])

            if key_exists(INTERACT, follow):
                self.__set_interact(follow[INTERACT])

            if key_exists(SLEEP_DELAY, follow):
                self.__set_sleep_delay(follow[SLEEP_DELAY])

        self.__session = session
        if key_not_exists(BY_TAGS, config[FOLLOW]):
            print('[INFO]: Follow with usernames...')
            self.__follow()
        elif key_not_exists(USERNAMES, config[FOLLOW]):
            FollowByTags(follow[BY_TAGS], session)

    def __follow(self) -> None:
        if self.__enable:
            self.__session.follow_user_followers(
                usernames=self.__usernames,
                amount=self.__amount,
                randomize=self.__randomize,
                interact=self.__interact,
                sleep_delay=self.__sleep_delay
            )

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
