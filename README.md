# MiniPFC
Code and instructions for Installing.
It is mostly a collection of python code that runs on a Raspberry Pi (or similar device).  See the OpenAg [forums](http://forum.openag.media.mit.edu/) for discussion and issues:


The MiniPFC is a simplified version of the MIT OpenAg Food Computer.




Code Structure -
```
|____.gitignore
|____config
| |____pin.json
| |____recipe.json
|
|____dump
| |____images/
|
|____modules
| |______init__.py
| |____camera.py
| |____fan.py
| |____light.py
| |____pump.py
| |____sensor.py
|
|____scripts
| |____capture-image.sh
|
|____tasks
| |______init__.py
| |____actuate.py
| |____learn.py
| |____sense.py
|
|____app.py
|____db.py
|____test.py
|____LICENSE
|____README.md
```

Use config/pin.json to modify pin connections to relays
Use config/recipe.json to edit recipie parameters
Use db.py to replace the database name from test to database name in your local couchdb

## Hardware Build:

**Fan:**
There are two fans, one for circulation and one for exhausting excess heat  These can run off the Raspberry's 5V or from a external 12V transformer

**Temperature/Humidity Sensor**
A si7021 sensor on an I2C bus is used for temperature and humidity.  See the following for (instructions)[https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/overview] on use and wiring.

**Webcam**
A standard USB camera is used for imaging (though the Raspberry Pi camera is an option).  See [here](https://www.raspberrypi.org/documentation/usage/webcams/) for instructions

**Relay**
A set of relays controled by GPIO pins is used to turn lights on and off (120V), and the exhaust fan (12V)

# Pin Assignment:
Refer to the following [diagram](https://docs.particle.io/datasheets/raspberrypi-datasheet/#pin-out-diagram) for the Raspberry's pin names:

Code follows the board number convention.

- '3 - SDA to si7021'
- '5 - SCL to si7021'
- '29 - light relay (relay #4)'
- '31 - (reserved for relay #3)'
- '33 - (reserved for relay #2)'
- '35 - GPIO13 fan control (relay #1)'


## Build Activities
### Assumptions:
1. NOOB install of Raspbian on Raspberry Pi
2. The Raspbian system has been configured 
    - for localization (time, timezone)
    - wifi is established and connected
    - I2C has been enabled
2. 32G SD card to hold data
3. Sensors and relay are wired to the Pi.  If you try to run the code without sensors, some of it will error out (I/O Error, I noticed in the getTempC() function).

### Software Build Steps

- Requirements
    python 2.7
    pip 9.0
    couchdb >= 1.6.0


 - Install fswebcam
    > sudo apt-get install fswebcam

- Download code from [Github](https://github.com/w0w/miniPFC).  Click on the zip file to open it, and move the files to the appropriate location.

    > cd ~/path_to_cloned_dir

    > pip install -r requirements.txt

- To run the application
    > python app.py
- To run the application in background
    >python app.py&



## Bill of Materials:
- Raspberry Pi
- 32G SD card
- SI7021 temperature/humidity sensor
- Wire or jumpers
- Relay

## To Do:
- Write test cases
- Implement Learn Module
- Improve acutation and recipie implementation
- One line installation and setup script
- Service to run app.py on system boot
- Find better way to construct eventData object in sense.py
