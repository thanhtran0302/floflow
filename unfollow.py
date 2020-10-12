from typing import List
from constants import RANDOM, AMOUNT, CUSTOM_LIST, CUSTOM_LIST_ENABLED, \
    INSTAPY_FOLLOWED_ENABLED, INSTAPY_FOLLOWED_PARAM, STYLE, SLEEP_DELAY, \
    DELAY_FOLLOWBACKERS, UNFOLLOW_AFTER, NON_FOLLOWERS, ALL_FOLLOWING, ALL, \
    ENABLE, CUSTOM_LIST_PARAM, NONFOLLOWERS, WHITE_LIST, UNFOLLOW
from sys import exit
from utils import key_exists


class Unfollow:
    __white_list: List[str] = []
    __enable: bool = False
    __amount: int = 10
    __custom_list_enabled: bool = False
    __custom_list: List[str] = []
    __custom_list_param: str = ALL
    __instapy_followed_enabled: bool = False
    __instapy_followed_param: str = ALL
    __nonFollowers: bool = False
    __allFollowing: bool = False
    __style: str = RANDOM
    __unfollow_after: int = None
    __delay_followbackers: int = 0
    __sleep_delay: int = 600
    __session = None

    def __init__(self, config: object, session):
        if key_exists(UNFOLLOW, config):
            unfollow = config[UNFOLLOW]
            print(unfollow)
            if key_exists(WHITE_LIST, unfollow):
                self.__set_white_list(unfollow[WHITE_LIST])
            if key_exists(ENABLE, unfollow):
                self.__enable = unfollow[ENABLE]
            if key_exists(AMOUNT, unfollow):
                self.__set_amount(unfollow[AMOUNT])
            if key_exists(CUSTOM_LIST_ENABLED, unfollow):
                self.__set_custom_list_enabled(unfollow[CUSTOM_LIST_ENABLED])
            if key_exists(CUSTOM_LIST, unfollow):
                self.__set_custom_list(unfollow[CUSTOM_LIST])
            if key_exists(CUSTOM_LIST_PARAM, unfollow):
                self.__set_custom_list_param(unfollow[CUSTOM_LIST_PARAM])
            if key_exists(INSTAPY_FOLLOWED_ENABLED, unfollow):
                self.__set_instapy_followed_enabled(
                    unfollow[INSTAPY_FOLLOWED_ENABLED]
                )
            if key_exists(INSTAPY_FOLLOWED_PARAM, unfollow):
                self.__set_instapy_followed_param(
                    unfollow[INSTAPY_FOLLOWED_PARAM]
                )
            if key_exists(NON_FOLLOWERS, unfollow):
                self.__set_non_followers(unfollow[NON_FOLLOWERS])
            if key_exists(ALL_FOLLOWING, unfollow):
                self.__set_all_following(unfollow[ALL_FOLLOWING])
            if key_exists(STYLE, unfollow):
                self.__set_style(unfollow[STYLE])
            if key_exists(UNFOLLOW_AFTER, unfollow):
                self.__set_unfollow_after(unfollow[UNFOLLOW_AFTER])
            if key_exists(DELAY_FOLLOWBACKERS, unfollow):
                self.__set_delay_followbackers(unfollow[DELAY_FOLLOWBACKERS])
            if key_exists(SLEEP_DELAY, unfollow):
                self.__set_sleep_delay(unfollow[SLEEP_DELAY])
        self.__session = session
        self.__unfollow()

    def __unfollow(self) -> None:
        if self.__enable:
            print('[INFO]: Start unfollowing...')
            if len(self.__white_list) >= 1:
                print('[INFO]: white_list -> ' + str(self.__white_list))
                self.__session.set_dont_include(friends=self.__white_list)
            self.__session.unfollow_users(
                amount=self.__amount,
                custom_list_enabled=self.__custom_list_enabled,
                custom_list=self.__custom_list,
                custom_list_param=self.__custom_list_param,
                instapy_followed_enabled=self.__instapy_followed_enabled,
                instapy_followed_param=self.__instapy_followed_param,
                nonFollowers=self.__nonFollowers,
                allFollowing=self.__allFollowing,
                style=self.__style,
                unfollow_after=self.__unfollow_after,
                delay_followbackers=self.__delay_followbackers,
                sleep_delay=self.__sleep_delay
            )

    def __set_style(self, style: str) -> None:
        if style is not FIFO or style is not LIFO or style is not RANDOM:
            exit('[ERROR]: style should be FIFO, LIFO, or RANDOM.')
        self.__style = style

    def __set_white_list(self, white_list: List[str]) -> None:
        if type(white_list) is not list:
            exit('[ERROR]: white_list should be a List[str] type')
        self.__white_list = white_list

    def __set_amount(self, amount: int) -> None:
        if type(amount) is not int:
            exit('[ERROR]: amount should be an int type.')
        self.__amount = amount

    def __set_custom_list_enabled(self, custom_list_enabled: bool) -> None:
        if type(custom_list_enabled) is not bool:
            exit('[ERROR]: custom_list_enabled should be a bool type.')
        self.__custom_list_enabled = custom_list_enabled

    def __set_custom_list(self, custom_list: List[str]) -> None:
        if type(custom_list) is not list:
            exit('[ERROR]: custom_list should be a List[str] type')
        self.__custom_list = custom_list

    def __set_custom_list_param(self, custom_list_param: str) -> None:
        if custom_list_param != ALL or custom_list_param != NONFOLLOWERS:
            exit('[ERROR]: custom_list_pram should be "all" or "nonfollowers"')
        self.__custom_list_param = custom_list_param

    def __set_instapy_followed_enabled(self, instapy_followed_enabled: bool) -> None:
        if type(instapy_followed_enabled) is not bool:
            exit('[ERROR]: instapy_followed_enabled should be a bool type.')
        self.__instapy_followed_enabled = instapy_followed_enabled

    def __set_instapy_followed_param(self, instapy_followed_param: str) -> None:
        if type(instapy_followed_param) is not str:
            exit('[ERROR]: instapy_followed_param should be an str type')
        self.__instapy_followed_param = instapy_followed_param

    def __set_non_followers(self, non_followers: bool) -> None:
        if type(non_followers) is not bool:
            exit('[ERROR]: non_followers should be a bool type')
        self.__nonFollowers = non_followers

    def __set_all_following(self, all_following: bool) -> None:
        if type(all_following) is not bool:
            exit('[ERROR]: all_following should be a bool type')
        self.__allFollowing = all_following

    def __set_unfollow_after(self, unfollow_after: int) -> None:
        if type(unfollow_after) is not int:
            exit('[ERROR]: unfollow_after should be an int type')
        self.__unfollow_after = unfollow_after

    def __set_delay_followbackers(self, delay_followbackers: int) -> None:
        if type(delay_followbackers) is not int:
            exit('[ERROR]: delay_followbackers should be an int type')
        self.__delay_followbackers = delay_followbackers

    def __set_sleep_delay(self, sleep_delay: int) -> None:
        if type(sleep_delay) is not int:
            exit('[ERROR]: sleep_delay should be an int type')
        self.__sleep_delay = sleep_delay
