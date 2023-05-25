#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import time

from PIL import Image

assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
hardware_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'hardware')

if os.path.exists(hardware_dir):
    sys.path.append(hardware_dir)
    
from waveshare_epd import epd7in5_V2

logging.basicConfig(level=logging.INFO)

filenames = [
    'alvvays_antisocialites.jpg',
    'ethel_cain_preachers_daughter.jpg',
    'phoebe_bridgers_punisher.jpg'
]

try:
    epd = epd7in5_V2.EPD()
    
    logging.info("Initializing")
    epd.init()
    epd.Clear()

    for filename in filenames:
        logging.info("Displaying " + filename)
        img_to_render = Image.open(os.path.join(assets_dir, filename))
        epd.display(epd.getbuffer(img_to_render))
        time.sleep(30)
        epd.init()
        epd.Clear()

    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("Force closing script")
    epd7in5_V2.epdconfig.module_exit()
    exit()
