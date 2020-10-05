from typing import List


class Account:
    __username: str = None
    __password: str = None
    __accounts_to_follow: List[str] = []

    def __init__(self, account):
        self.__username = account['username']
        self.__password = account['password']
        self.__accounts_to_follow = account['accounts_to_follow']

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_accounts_to_follow(self):
        return self.__accounts_to_follow
