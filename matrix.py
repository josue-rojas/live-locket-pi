#!/usr/bin/env python3
import sqlite3
con = sqlite3.connect("images.db")
cur = con.cursor()

res = cur.execute("SELECT * FROM images")
res.fetchall()

# import time
# import sys
# import requests
# from io import BytesIO
# import sys,os

# # from rgbmatrix import RGBMatrix, RGBMatrixOptions
# # from PIL import Image
# # from datetime import datetime
# # import configparser



# # # default image
# dir = os.path.dirname(__file__)
# filename = os.path.join(dir, './config/rgb_options.ini')
# config = configparser.ConfigParser()
# config.read(filename)
# # image_file = os.path.join(dir, './default.png')


# options = RGBMatrixOptions()
# options.hardware_mapping = 'adafruit-hat' 
# options.rows = int(config['DEFAULT']['rows'])
# options.cols = int(config['DEFAULT']['columns'])
# options.chain_length = int(config['DEFAULT']['chain_length'])
# options.parallel = int(config['DEFAULT']['parallel'])
# options.hardware_mapping = config['DEFAULT']['hardware_mapping']
# options.gpio_slowdown = int(config['DEFAULT']['gpio_slowdown'])
# options.brightness = int(config['DEFAULT']['brightness'])
# options.limit_refresh_rate_hz = int(config['DEFAULT']['refresh_rate'])


# # image = Image.open(image_file)

# # matrix = RGBMatrix(options=options)

# # # Create a thumbnail that first our screen
# # image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# # matrix.SetImage(image.convert('RGB'))

# # try:
# #     print("Press CTRL-C to stop.")
# #     while True:
# #         try:
# #             now = datetime.now()
# #             current_time = now.strftime("%H:%M:%S")
# #             print("Current Time =", current_time)
# #             # request data location and settings
# #             response = requests.get('https://live-locket.netlify.app/.netlify/functions/getSettings', timeout=10, verify=False)
# #             responseOptions = response.json()
# #             imageSrc = responseOptions['imageSrc']
# #             # request  image
# #             print('downloading....')
# #             print(imageSrc)
# #             imageReq = requests.get(imageSrc)
# #             #
# #             _image = Image.open(BytesIO(imageReq.content))
# #             _image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# #             matrix.SetImage(_image.convert('RGB'))
# #             print('setting image')
# #         except Exception as e:
# #             print(e)
# #             print('errrorr')
# #             matrix.SetImage(image.convert('RGB'))
# #         time.sleep(1800)
# # except KeyboardInterrupt:
# #     sys.exit(0)
