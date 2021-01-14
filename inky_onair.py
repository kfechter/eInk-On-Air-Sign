#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky.auto import auto
from inky.eeprom import read_eeprom
import signal
import RPi.GPIO as GPIO

# Identify the display for debugging purposes
display = read_eeprom()
if display is None:
    print("Display does not have readable eeprom: possibly older hat model")
else:
    print("Found: {}".format(display.get_variant()))
    print(display)

try:
    inky_display = auto(ask_user=True, verbose=True)
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

# Change this to change your Name/Handle
Name = "TheSecondKen"

#MQTTSettings
MQTTBroker = ""
MQTTTopic = ""


# Set up buttons and power pin
BUTTONS = [4, 5, 6, 16, 24]
LABELS = ['Pwr', 'A', 'B', 'C', 'D']
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    print("Button press detected on pin: {} label: {}".format(pin, label))

for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=250)




signal.pause()