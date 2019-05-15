#!/usr/bin/env python

import os
from honeydb import api

API_ID = os.environ['HONEYDB_API_ID']
API_KEY = os.environ['HONEYDB_API_KEY']

honeydb = api.Client(API_ID, API_KEY)

for badhost in honeydb.bad_hosts():
    if int(badhost['count']) > 5:
        print("Remote host: {}\tLast seen: {}".format(badhost['remote_host'],
                                                      badhost['last_seen']))
