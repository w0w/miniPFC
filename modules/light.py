import RPi.GPIO as GPIO
import json
def loadConfig():

    with open('./config/pin.json') as data_file:    
        data = json.load(data_file)
        return data


config = loadConfig()

def setLightOff():
    "Turn off light relay"
    lightPin = config['lightPin']
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("Turn lights off")
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.output(lightPin, GPIO.HIGH)


def setLightOn():
    "Turn on light relay"
    lightPin = config['lightPin']
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print ("Turn lights on")
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.output(lightPin, GPIO.LOW)