import json
import RPi.GPIO as GPIO
from modules.sensor import getTempC, getHumidity
def loadConfig():
    with open('./config/pin.json') as data_file:    
        data = json.load(data_file)
        return data


currentPins = loadConfig().values()

def bootActuators():
    '''Assumes that pi is booting and set off all the relays'''
    GPIO.setmode(GPIO.BOARD)
    for i, p in enumerate(currentPins):
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.HIGH)
        print(p, GPIO.input(p))
    print('Actuators turned off')


bootActuators()