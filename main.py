#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

import praw

parser = argparse.ArgumentParser()

parser.add_argument("--title", help="Post title", required=True)
parser.add_argument("--message", help="Post message", required=True)
parser.add_argument(
    "--subreddit",
    help="Subreddit to post (default $REDDIT_SUBREDDIT)",
    required=False,
)


def get_reddit_client(subreddit: str = None):
    CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
    CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
    USERNAME = os.environ["REDDIT_USERNAME"]
    PASSWORD = os.environ["REDDIT_PASSWORD"]
    USER_AGENT = os.getenv("REDDIT_USER_AGENT", f"script by u/{USERNAME}")

    SUBREDDIT_ENV = os.getenv("REDDIT_SUBREDDIT", "test")

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD,
    )

    return reddit.subreddit(subreddit or SUBREDDIT_ENV)


if __name__ == "__main__":
    args = parser.parse_args()
    TITLE = args.title
    MESSAGE = args.message

    rv = get_reddit_client(args.subreddit).submit(
        TITLE, selftext=MESSAGE, send_replies=False
    )

    print(("Post submitted successfully!", rv))
