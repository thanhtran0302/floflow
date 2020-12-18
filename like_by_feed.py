from utils import key_exists
from constants import AMOUNT, INTERACT, UNFOLLOW, RANDOMIZE, ENABLE, LIKE_BY_FEED


class LikeByFeed:
    __amount: int = 0
    __randomize: bool = True
    __interact: bool = True
    __unfollow: bool = True
    __session = None

    def __init__(self, config: object, session):
        if config[LIKE_BY_FEED] and config[LIKE_BY_FEED][ENABLE]:
            local_config = config[LIKE_BY_FEED]

            if key_exists(AMOUNT, local_config):
                self.__amount = local_config[AMOUNT]

            if key_exists(INTERACT, local_config):
                self.__interact = local_config[INTERACT]

            if key_exists(RANDOMIZE, local_config):
                self.__randomize = local_config[RANDOMIZE]

            if key_exists(UNFOLLOW, local_config):
                self.__unfollow = local_config[UNFOLLOW]

            self.__session = session
            self.__like_by_feed()

    def __like_by_feed(self) -> None:
        self.__session.like_by_feed(
            amount=self.__amount,
            randomize=self.__randomize,
            unfollow=self.__unfollow,
            interact=self.__interact
        )
