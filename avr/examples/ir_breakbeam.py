import RPi.GPIO as GPIO
import board
import neopixel
from adafruit_led_animation.animation.solid import Solid

from adafruit_led_animation.color import (
    PURPLE,
    BLACK
)

BEAM_PIN = 22
PIXEL_PIN = board.D12
NUM_PIXELS = 45
PIXEL_ORDER = neopixel.GRB
PIXELS = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=PIXEL_ORDER)

def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        solid = Solid(PIXELS, color=PURPLE)
        solid.animate()
    else:
        solid = Solid(PIXELS, color=BLACK)
        solid.animate()

GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

message = input("Press enter to quit\n\n") 
GPIO.cleanup()