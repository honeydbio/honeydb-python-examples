#!/usr/bin/env python

import os
from honeydb import api

API_ID = os.environ["HONEYDB_API_ID"]
API_KEY = os.environ["HONEYDB_API_KEY"]
MIN_COUNT = 10

honeydb = api.Client(API_ID, API_KEY)

for badhost in honeydb.bad_hosts():
    if int(badhost["count"]) >= MIN_COUNT:
        print(
            f"Remote host: {badhost['remote_host']}\tLast seen: {badhost['last_seen']}"
        )
