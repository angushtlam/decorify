#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import time

from PIL import Image
from waveshare_epd import epd7in5_V2

assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

logging.basicConfig(level=logging.DEBUG)

filenames = ['alvvays_blue_rev.bmp']

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
