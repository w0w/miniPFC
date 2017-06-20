import RPi.GPIO as GPIO
import json
def loadConfig():

    with open('./config/pin.json') as data_file:    
        data = json.load(data_file)
        return data


config = loadConfig()

def setPumpOff():
    "Turn pump off"
    pumpPin = config["pumpPin"]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("pump off")
    GPIO.setup(pumpPin, GPIO.OUT)
    GPIO.output(pumpPin, GPIO.HIGH)


def setPumpOn():
    "Turn pump on"
    pumpPin = config["pumpPin"]
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("pump on")
    GPIO.setup(pumpPin, GPIO.OUT)
    GPIO.output(pumpPin, GPIO.LOW)
