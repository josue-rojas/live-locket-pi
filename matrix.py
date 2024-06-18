#!/usr/bin/env python3

import os
import sys
import time
from datetime import datetime
from configparser import ConfigParser

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

from imageRepository import get_random_image
from constants import IMAGES_DIR, CONFIG_SRC

def get_next_random_file(current_file):
    next_file = current_file
    while current_file == next_file:
        next_file = get_random_image()[3]
    return next_file

def configure_matrix(config):
    options = RGBMatrixOptions()
    options.hardware_mapping = config['DEFAULT'].get('hardware_mapping', 'adafruit-hat')
    options.rows = config['DEFAULT'].getint('rows', 32)
    options.cols = config['DEFAULT'].getint('columns', 32)
    options.chain_length = config['DEFAULT'].getint('chain_length', 1)
    options.parallel = config['DEFAULT'].getint('parallel', 1)
    options.gpio_slowdown = config['DEFAULT'].getint('gpio_slowdown', 2)
    options.brightness = config['DEFAULT'].getint('brightness', 100)
    options.limit_refresh_rate_hz = config['DEFAULT'].getint('refresh_rate', 0)
    return options

def main():
    dir = os.path.dirname(__file__)

    # Load configuration
    config_file_path = os.path.join(dir, CONFIG_SRC)
    config = ConfigParser()
    config.read(config_file_path)

    # Initial image setup
    start_image = get_random_image()[3]
    image_file_path = os.path.join(dir, IMAGES_DIR, start_image)
    
    # Configure RGB matrix
    options = configure_matrix(config)
    matrix = RGBMatrix(options=options)

    # Display the initial image
    image_timer = config['DEFAULT'].getint('image_timer', 5)
    image = Image.open(image_file_path)
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    matrix.SetImage(image.convert('RGB'))

    try:
        print("Press CTRL-C to stop.")
        current_file = start_image

        while True:
            try:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)

                current_file = get_next_random_file(current_file)
                current_image_file_path = os.path.join(dir, IMAGES_DIR, current_file)
                next_image = Image.open(current_image_file_path)

                next_image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
                matrix.SetImage(next_image.convert('RGB'))
                print('Setting image:', current_file)
            except Exception as e:
                print("Error setting image:", e)
                matrix.SetImage(image.convert('RGB'))

            time.sleep(image_timer)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
