from utils import key_exists
from constants import AMOUNT, RANDOMIZE, ENABLE, LIKE_BY_USERS, MEDIA


class LikeByUsers:
    __amount: int = 15
    __randomize: bool = True
    __media: str = 'Photo'
    __session = None
    __users = []

    def __init__(self, config: object, session, users: list):
        if config[LIKE_BY_USERS] and config[LIKE_BY_USERS][ENABLE]:
            local_config = config[LIKE_BY_USERS]

            if key_exists(AMOUNT, local_config):
                self.__amount = local_config[AMOUNT]

            if key_exists(RANDOMIZE, local_config):
                self.__randomize = local_config[RANDOMIZE]

            if key_exists(MEDIA, local_config):
                self.__media = local_config[MEDIA]

            self.__users = users
            self.__session = session
            self.__like_by_feed()

    def __like_by_feed(self) -> None:
        self.__session.like_by_users(
            amount=self.__amount,
            randomize=self.__randomize,
            media=self.__media,
            usernames=self.__users
        )
