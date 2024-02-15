#!/usr/bin/env python

import os
from honeydb import api

MIN_COUNT = 10
SERVICE = "VNC"
API_ID = os.environ["HONEYDB_API_ID"]
API_KEY = os.environ["HONEYDB_API_KEY"]

honeydb = api.Client(API_ID, API_KEY)

for badhost in honeydb.bad_hosts(service=SERVICE):
    if int(badhost["count"]) >= MIN_COUNT:
        print(f"{SERVICE} from: {badhost['remote_host']} ({badhost['count']})")
