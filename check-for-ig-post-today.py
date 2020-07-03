import os
import datetime

import sentry_sdk
from instabot import Bot

ENV_SENTRY_DSN = 'SENTRY_DSN'
ENV_USERNAME = 'ig_username'
ENV_PASSWORD = 'ig_password'
ENV_USERNAME_TO_CHECK = 'USERNAME_TO_CHECK'

SECONDS_IN_MINUTE = MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24


def main():
    if ENV_SENTRY_DSN in os.environ:
        sentry_sdk.init(os.environ[ENV_SENTRY_DSN])

    raise Exception("test exception 123")

    bot = Bot()
    bot.login(username=os.environ[ENV_USERNAME], password=os.environ[ENV_PASSWORD])
    medias = bot.get_total_user_medias(os.environ[ENV_USERNAME_TO_CHECK])
    taken_at = datetime.datetime.fromtimestamp(bot.get_media_info(medias[0])[0]['taken_at'])

    now = datetime.datetime.now()

    hours_since_last_post = (now - taken_at).seconds / (SECONDS_IN_MINUTE * MINUTES_IN_HOUR)

    if hours_since_last_post > HOURS_IN_DAY:
        raise Exception("It's been " + str(hours_since_last_post) + " hours since the last post!")
    else:
        print("It's been " + str(hours_since_last_post) + " hours since the last post 😊")


if __name__ == '__main__':
    main()
