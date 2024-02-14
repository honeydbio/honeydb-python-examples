#!/usr/bin/env python

import os
from honeydb import api

API_ID = os.environ["HONEYDB_API_ID"]
API_KEY = os.environ["HONEYDB_API_KEY"]

honeydb = api.Client(API_ID, API_KEY)

print(honeydb.bad_hosts())
