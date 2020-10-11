from instapy import InstaPy
from instapy import smart_run
from account import Account
import random
import json
import sys

comments = [
    'Nice shot! @{}',
    'I love your profile! @{}',
    '@{} Love it!',
    '@{} :heart::heart:',
    '@{}:revolving_hearts::revolving_hearts:',
    '@{}:fire::fire::fire:'
]

if len(sys.argv) <= 1:
    sys.exit(
        '[ERROR]: Please provide the instagram account that you want to use (match with accounts.json)')

account = None
try:
    with open('accounts.json', 'r') as data:
        formatted_data = json.load(data)

        if sys.argv[1] not in formatted_data:
            sys.exit('[ERROR]: given account is not exists.')
        account = Account(formatted_data[sys.argv[1]])
except:
    sys.exit('[ERROR]: accounts.json file not found.')

session = InstaPy(
    username=account.get_username(),
    password=account.get_password(),
    headless_browser=False,
    multi_logs=True,
    disable_image_load=True
)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=15000,
        max_following=1500,
        min_followers=0,
        min_following=30
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

    follow = account.get_follow()
    if follow != None and follow.get_enable():
        session.follow_user_followers(
            usernames=follow.get_usernames(),
            amount=follow.get_amount(),
            randomize=follow.get_randomize(),
            interact=follow.get_interact(),
            sleep_delay=follow.get_sleep_delay()
        )
    else:
        print('[INFO]: follow feature is not enable.')
