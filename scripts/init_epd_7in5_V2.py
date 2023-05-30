#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import sys
import time


# Append library files the system path so this file can import those files.
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from decorify import Decorify
from waveshare_epd import epd7in5_V2


logging.basicConfig(level=logging.INFO)

# Create a Decorify state machine
decorify_obj = Decorify()

try:
    epd = epd7in5_V2.EPD()

    logging.info("Initializing…")
    epd.init()
    epd.Clear()

    while True:
        img_to_render = decorify_obj.get_image()
        epd.display(epd.getbuffer(img_to_render))
        time.sleep(10)

        # Display the next image
        decorify_obj.next_image()    

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("Force closing script")
    epd7in5_V2.epdconfig.module_exit()
    exit()
