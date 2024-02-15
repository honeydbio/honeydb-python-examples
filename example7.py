#!/usr/bin/env python

import os
import datetime
from honeydb import api

EVENT = "RX"
SERVICE = "HTTP"

API_ID = os.environ["HONEYDB_API_ID"]
API_KEY = os.environ["HONEYDB_API_KEY"]

honeydb = api.Client(API_ID, API_KEY)
today = datetime.datetime.today()
from_id = None  # initialize from_id to None

while from_id != 0:
    """
    Sensor data returns an array with two objects:
    [
        {"data": []}
        {"from_id": 0}
    ]
    """
    sensor_data = honeydb.sensor_data(
        sensor_data_date=today.strftime("%Y-%m-%d"), from_id=from_id
    )

    for event in sensor_data[0]["data"]:
        if event["event"] == EVENT and event["service"] == SERVICE:
            byte_data = bytes.fromhex(event["data"])
            print(f"{byte_data.decode()}")

    from_id = int(sensor_data[1]["from_id"])
