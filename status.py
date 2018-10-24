#! /usr/bin/env python3
from time import sleep
from sense_hat import SenseHat
import requests
sense = SenseHat()

def happy():
    sense.clear((0,10,0))
    sense.set_pixel(2, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (0, 0, 255))
    sense.set_pixel(3, 4, (100, 0, 0))
    sense.set_pixel(1, 5, (255, 0, 0))
    sense.set_pixel(2, 6, (255, 0, 0))
    sense.set_pixel(3, 6, (255, 0, 0))
    sense.set_pixel(4, 6, (255, 0, 0))
    sense.set_pixel(5, 5, (255, 0, 0))

def medium():
    sense.clear((0,10,0))
    sense.set_pixel(2, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (0, 0, 255))
    sense.set_pixel(3, 4, (100, 0, 0))
    sense.set_pixel(1, 6, (200, 0, 0))
    sense.set_pixel(2, 6, (200, 0, 0))
    sense.set_pixel(3, 6, (200, 0, 0))
    sense.set_pixel(4, 6, (200, 0, 0))
    sense.set_pixel(5, 6, (200, 0, 0))


def sad():
    sense.clear((0,10,0))
    sense.set_pixel(2, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (0, 0, 255))
    sense.set_pixel(3, 4, (100, 0, 0))
    sense.set_pixel(1, 7, (200, 0, 0))
    sense.set_pixel(2, 6, (200, 0, 0))
    sense.set_pixel(3, 6, (200, 0, 0))
    sense.set_pixel(4, 6, (200, 0, 0))
    sense.set_pixel(5, 7, (200, 0, 0))

sense.set_rotation(180)

while True:
    sense.set_pixel(0, 0, (0, 0, 128))
    r = requests.get('https://app-r.referens.sys.kth.se/lms-monitor-of-monitor/api')
    sense.clear((0,0,0))
    if r.status_code != 200:
        sense.clear((255,0,0))
        sense.show_message("%s" % r.status_code)
    else:
        json = r.json()
        if any(part.get('color') == 'red' for part in json):
            sad()
        elif all(part.get('color') == 'blue' for part in json):
            happy()
        else:
            medium()
    sleep(1.0)
