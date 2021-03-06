#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
import base64
import uuid
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                os.path.pardir)))

from datetime import datetime
from dateutil.tz import tzlocal
from modules.sensor import getTempC, getHumidity
from modules.camera import captureImage
from db import bulkStore

S3_BASEURL = 'https://s3.ap-south-1.amazonaws.com/s-webcam-images/F5qkMpjxTKDgAcknk8d%2Bhfyt%2BL9fI8xtvBu636Nr/'

# Get the current date/time with the timezone.

def loadConfig():
    with open('./config/recipe.json') as data_file:
        data = json.load(data_file)
        return data


config = loadConfig()

deviceID = '0000ad19b01'
pID = os.getpid()
appID = 1


# get a UUID - URL safe, Base64

def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '')


def capture():
    temp = getTempC()
    hum = getHumidity()
    eventID = get_a_uuid()
    imgName = config['PlantName'] + eventID
    captureImage(imgName)
    imgPath = S3_BASEURL + imgName + '.jpg'
    createdAt = str(datetime.now(tzlocal()))
    eventData = [{
        'appID': appID,
        'pID': pID,
        'deviceID': deviceID,
        'eventID': eventID,
        'temp': temp,
        'hum': hum,
        'imgPath': imgPath,
        'createdAt': createdAt,
        }]
    bulkStore(eventData)



			