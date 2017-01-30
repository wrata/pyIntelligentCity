#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pyIntelligentCity
from time import sleep
   
city = pyIntelligentCity.pyIntelligentCity('COM5')
city.info()

# na próbę pomigamy żółtym światłem
x = city.SD_yellow_blink()
if x == 4:
    print 'Sygnalizator drogowy nie jest podłączony'
else: 
    print 'Sygnalizator drogowy - port: ', x
    city.SD_all_off()
    for i in range(5):
        city.SD_red_on()
        sleep(3)
        city.SD_red_off()
        city.SD_yellow_on()
        sleep(1)
        city.SD_yellow_off()
        city.SD_green_on()
        sleep(1)
print('--- za 5 s zamykamy ---')
sleep(5)
city.close()


