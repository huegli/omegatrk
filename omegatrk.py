#!/usr/bin/env python
from __future__ import print_function

import json
import subprocess
import time

from OmegaExpansion import oledExp

oledExp.driverInit()

while (1):
    s = subprocess.Popen("ubus call gps info", shell=True, stdout=subprocess.PIPE).stdout.read()
    d = json.loads(s)

    #with open('one_ogps.json') as f:
    #    d = json.load(f)
    
    if (('signal' in d) and (not d['signal'])):
        lat = 0.0
        lon = 0.0
        dly = 60
    else:
        lat = round(float(d['latitude']),3)
        lon = round(float(d['longitude']),3)
	dly = 10

    latstr = 'LAT: {:8.3f}'.format(lat)
    lonstr = 'LON: {:8.3f}'.format(lon)

    print(latstr)
    print(lonstr)

    oledExp.clear()
    oledExp.setCursor(1,1)
    oledExp.write(latstr)
    oledExp.setCursor(3,1)
    oledExp.write(lonstr)

    time.sleep(dly)
