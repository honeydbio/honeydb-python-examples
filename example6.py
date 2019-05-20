#!/usr/bin/env python

import os
import datetime
from honeydb import api

API_ID = os.environ['HONEYDB_API_ID']
API_KEY = os.environ['HONEYDB_API_KEY']

honeydb = api.Client(API_ID, API_KEY)
today = datetime.datetime.today()
from_id = -1

while from_id != 0:
    if from_id == -1:
        from_id = None

    """
    Sensor data returns an array with two objects:
    {u'data': []}
    {u'from_id': 0}
    """
    sensor_data = honeydb.sensor_data(sensor_data_date=today.strftime('%Y-%m-%d'), from_id=from_id)

    print(sensor_data[1]['from_id'])

    for event in sensor_data[0]['data']:
        if event['event'] == 'RX' and event['service'] == 'HTTP':
            print("{}".format(event['data'].decode('hex')))

    from_id = int(sensor_data[1]['from_id'])
