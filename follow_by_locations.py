from typing import List
from utils import key_exists
from constants import LOCATIONS, AMOUNT, MEDIA, SKIP_TOP_POSTS


class FollowByLocations:
    __locations: List[str] = []
    __amount: int = 15
    __media: str = None
    __skip_top_posts: bool = True
    __session = None

    def __init__(self, config: object, session):
        if config:
            if key_exists(LOCATIONS, config):
                self.__locations = config[LOCATIONS]
            if key_exists(AMOUNT, config):
                self.__amount = config[AMOUNT]
            if key_exists(MEDIA, config):
                self.__media = config[MEDIA]
            if key_exists(SKIP_TOP_POSTS, config):
                self.__skip_top_posts = config[SKIP_TOP_POST]

        self.__session = session
        self.__follow_by_locations()

    def __follow_by_locations(self) -> None:
        print('[INFO]: Follow by locations -> ' + str(self.__locations))
        self.__session.follow_by_locations(
            locations=self.__locations,
            amount=self.__amount,
            media=self.__media,
            skip_top_posts=self.__skip_top_posts
        )
