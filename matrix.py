#!/usr/bin/env python3
import sqlite3
import time
import sys
# import requests
from io import BytesIO
import sys,os

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from datetime import datetime
import configparser

IMAGES_DB = "images.db"
IMAGES_DIR = "./images"

CONFIG_SRC = './config/rgb_options.ini'

images = []

# def getImages(): 
#   if len(images):
#       return images
#   con = sqlite3.connect(IMAGES_DB)
#   cur = con.cursor()
#   res = cur.execute("SELECT * FROM images")
#   images = res.fetchall()

#   return images

def getRandomImage():
  con = sqlite3.connect(IMAGES_DB)
  cur = con.cursor()
  res = cur.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT 1;")
  
  return res.fetchone()



# def getStartImage():
#     con = sqlite3.connect(IMAGES_DB)
#     cur = con.cursor()
#     res = cur.execute("SELECT * FROM images where ID = 0")

#     return res.fetchone()

def getNextRandomFile(currentFile):
    nextFile = currentFile
    while currentFile == nextFile:
        nextFile = getRandomImage()[3]

    return nextFile


# # default image
dir = os.path.dirname(__file__)
filename = os.path.join(dir, CONFIG_SRC)
config = configparser.ConfigParser()
config.read(filename)
startImage = getRandomImage()[3]
image_file = os.path.join(dir, IMAGES_DIR, startImage)

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

image_timer = int(config['DEFAULT']['image_timer'])
image = Image.open(image_file)

matrix = RGBMatrix(options=options)

# # # Create a thumbnail that first our screen
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    currentFile = startImage
    while True:
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)

            currentFile = getNextRandomFile(currentFile)
            currentImageFilePath = os.path.join(dir, IMAGES_DIR, startImage)
            nextImage = Image.open(currentImageFilePath)

            nextImage.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
            matrix.SetImage(image.convert('RGB'))
            print('setting image', currentFile)
        except Exception as e:
            print(e)
            print('errrorr')
            matrix.SetImage(image.convert('RGB'))
        time.sleep(image_timer)
except KeyboardInterrupt:
    sys.exit(0)
