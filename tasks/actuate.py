import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from modules.fan import setFanOff, setFanOn
from modules.light import setLightOff, setLightOn
from modules.pump import setPumpOn, setPumpOff
from modules.sensor import getTempC, getHumidity


import datetime
t1= datetime.datetime.now()


import json
from pprint import pprint

import RPi.GPIO as GPIO

def loadPins():
	with open('./config/pin.json') as data_file:    
	    data = json.load(data_file)
	    return data

currentPins= loadPins().values()

def bootActuators():
	'''Assumes that pi is booting and set off all the relays'''
	GPIO.setmode(GPIO.BOARD)
	for i, p in enumerate(currentPins):
		GPIO.setup(p, GPIO.OUT)
		GPIO.output(p, GPIO.HIGH)
		print(p, GPIO.input(p))
	print('Actuators turned off')

bootActuators()

def loadConfig():
	print('...LoadingConfig')
	with open('./config/recipe.json') as data_file:    
	    data = json.load(data_file)
	    print('Config Loaded')
	    return data

config = loadConfig()


def lightDecision():
	if t1.hour >= config["LightOn"]:
		print("t1.hour")
		print(t1.hour)
		print("LightOn")
		print(config["LightOn"])
		setLightOn()
		print('Light on case 1')
	elif t1.hour >= config["LightOff"]:
		print("t1.hour")
		print(t1.hour)
		print("LightOff")
		print(config["LightOff"])
		setLightOff()
		print('Light off case 2')
	else:
		print("t1.hour")
		print(t1.hour)
		print("LightOn")
		print(config["LightOn"])
		print("LightOff")
		print(config["LightOff"])
		print('lightDecision nothing happened case 3')

def fanDecision():
	temp = getTempC()
	hum = getHumidity()
	if hum > config["HumMax"]:
		print("hum")
		print(hum)
		print("HumMax")
		print(config["HumMax"])
		setFanOn()
		print('setFanOn case 1')
		#Turn on dehumidifier
	elif hum < config["HumMin"]:
		print("hum")
		print(hum)
		print("HumMin")
		print(config["HumMin"])
		print('turn on humidifier case 2')
		#turn on humidifier
	elif hum > config["HumMin"] and hum < config["HumMax"]:
		print("hum")
		print(hum)
		print("HumMin")
		print(config["HumMin"])
		print("HumMax")
		print(config["HumMax"])
		print('fanDecision nothing happened case 3')
	else:
		print("hum")
		print(hum)
		print("HumMin")
		print(config["HumMin"])
		print("HumMax")
		print(config["HumMax"])
		print('fanDecision nothing happened case 4')

		

def everythingOn():
	setLightOn()
	setFanOn()
	setPumpOn()

def everythingOff():
	setLightOff()
	setFanOff()
	setPumpOff()

def recipe():
	lightDecision()
	fanDecision()
