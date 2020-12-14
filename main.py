from instapy import InstaPy
from instapy import smart_run
from account import Account
from follow import Follow
from unfollow import Unfollow
from utils import key_not_exists
import random
import json
import sys


if len(sys.argv) <= 1:
    sys.exit(
        '[ERROR]: Please provide the instagram account that you want to use (match with accounts.json)'
    )

account: Account = None
config: object = {}
instaname = sys.argv[1]

with open('accounts.json', 'r') as data:
    config = json.load(data)

    if key_not_exists(instaname, config):
        sys.exit('[ERROR]: ' + instaname + ' is not exists.')
    account = Account(config[instaname])

session = InstaPy(
    username=account.get_username(),
    password=account.get_password(),
    headless_browser=False,
    multi_logs=True,
    disable_image_load=True
)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True
    )

    session.set_quota_supervisor(
        enabled=True,
        sleep_after=["likes_h", "follows_h", "unfollows_h", "server_calls_h"],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes_hourly=57,
        peak_likes_daily=700,
        peak_follows_hourly=48,
        peak_follows_daily=None,
        peak_unfollows_hourly=35,
        peak_unfollows_daily=402,
        peak_server_calls_hourly=random.randint(150, 200),
        peak_server_calls_daily=4200
    )

    Follow(config[instaname], session)
    Unfollow(config[instaname], session)
