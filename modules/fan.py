import RPi.GPIO as GPIO
import json

def loadConfig():

    with open('./config/pin.json') as data_file:    
        data = json.load(data_file)
        return data


config = loadConfig()

def setFanOff():
    "Turn fan off"
    fanPin = config["fanOnePin"]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("Fan off")
    GPIO.setup(fanPin, GPIO.OUT)
    GPIO.output(fanPin, GPIO.HIGH)


def setFanOn():
    "Turn fan on"
    fanPin = config["fanOnePin"]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("Fan on")
    GPIO.setup(fanPin, GPIO.OUT)
    GPIO.output(fanPin, GPIO.LOW)
    
