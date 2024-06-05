#!/usr/bin/env python3
import time
import sys
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from datetime import datetime
import configparser
from imageRepository import get_random_image
from constants import IMAGES_DIR, CONFIG_SRC

def getNextRandomFile(currentFile):
    nextFile = currentFile
    while currentFile == nextFile:
        nextFile = get_random_image()[3]
    return nextFile

def load_config():
    dir = os.path.dirname(__file__)
    configFileName = os.path.join(dir, CONFIG_SRC)
    config = configparser.ConfigParser()
    config.read(configFileName)
    return config

def configure_matrix(config):
    options = RGBMatrixOptions()
    options.hardware_mapping = 'adafruit-hat' 
    options.rows = int(config['DEFAULT']['rows'])
    options.cols = int(config['DEFAULT']['columns'])
    options.chain_length = int(config['DEFAULT']['chain_length'])
    options.parallel = int(config['DEFAULT']['parallel'])
    options.hardware_mapping = config['DEFAULT']['hardware_mapping']
    options.gpio_slowdown = int(config['DEFAULT']['gpio_slowdown'])
    options.brightness = int(config['DEFAULT']['brightness'])
    options.limit_refresh_rate_hz = int(config['DEFAULT']['refresh_rate'])
    return RGBMatrix(options=options)

def display_image(matrix, image_path):
    image = Image.open(image_path)
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    matrix.SetImage(image.convert('RGB'))

def main():
    config = load_config()
    image_timer = int(config['DEFAULT']['image_timer'])
    matrix = configure_matrix(config)
    dir = os.path.dirname(__file__)

    startImage = get_random_image()[3]
    currentFile = startImage
    currentImageFilePath = os.path.join(dir, IMAGES_DIR, currentFile)

    display_image(matrix, currentImageFilePath)

    try:
        print("Press CTRL-C to stop.")
        while True:
            try:
                currentFile = getNextRandomFile(currentFile)
                currentImageFilePath = os.path.join(dir, IMAGES_DIR, currentFile)
                display_image(matrix, currentImageFilePath)
            except Exception as e:
                print("Error:", e)
                display_image(matrix, currentImageFilePath)
            time.sleep(image_timer)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
