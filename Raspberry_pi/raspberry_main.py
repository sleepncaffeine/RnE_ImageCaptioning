from keras.utils import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse
from subprocess import call
from picamera import PiCamera
from time import sleep
from gpiozero import Button

camera = PiCamera()
button = Button(2)
photo_name = "test.jpg"


def take_photo():
    camera.start_preview()
    sleep(1)
    camera.capture(f"home/pi/Desktop/{photo_name}")
    camera.stop_preview()


cmd_beg = "espeak "
cmd_end = " 2>/dev/null"


def speak(string):
    call([cmd_beg + string + cmd_end], shell=True)


speak("Hello, world!")
