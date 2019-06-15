#!/usr/bin/env python
from __future__ import print_function

import json
import pynmea2
import serial
import subprocess
import time

from OmegaExpansion import oledExp

oledExp.driverInit()
oledExp.clear()

port = "/dev/ttyACM0"
 
def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
	latstr = ' LAT: {} {}'.format(msg.lat, msg.lat_dir)
        lonstr = ' LON: {} {}'.format(msg.lon, msg.lon_dir)        
        satstr = '#SAT: {}'.format(msg.num_sats)
        timestr = 'TIME: {}'.format(msg.timestamp)
	oledExp.setCursor(1,1)
        oledExp.write(latstr)
        oledExp.setCursor(2,1)
        oledExp.write(lonstr)
        oledExp.setCursor(4,1)
        oledExp.write(satstr)
        oledExp.setCursor(5,1)
        oledExp.write(timestr)

 
 
serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)

