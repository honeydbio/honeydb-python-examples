#!/usr/bin/env python

import os
from honeydb import api

API_ID = os.environ["HONEYDB_API_ID"]
API_KEY = os.environ["HONEYDB_API_KEY"]

honeydb = api.Client(API_ID, API_KEY)

TOP_COUNT = 10

for host in honeydb.twitter_threat_feed():
    if int(host["count"]) > TOP_COUNT:
        print(
            "Remote host: {}\tLast seen: {}".format(
                host["remote_host"], host["last_seen"]
            )
        )
        for tweet in honeydb.twitter_threat_feed(ipaddress=host["remote_host"]):
            print(
                "\tUser: {}\tTweet: {}".format(
                    tweet["screen_name"], tweet["tweet_text"]
                )
            )
