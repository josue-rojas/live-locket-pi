#!/usr/bin/env python3
import time
from datetime import datetime
import configparser
import sys,os
import requests
from constants import CONFIG_SRC, GET_ALL_IMAGES_API, IMAGES_API_KEY, IMAGES_BUCKET_BASE, IMAGES_DIR


CONFIG_SRC = './config/rgb_options.ini'

dir = os.path.dirname(__file__)
configFileName = os.path.join(dir, CONFIG_SRC)
config = configparser.ConfigParser()
config.read(configFileName)

image_dowload_rate = int(config['DEFAULT']['image_dowload_rate'])

try:
  print("Press CTRL-C to stop.")

  while True:
    try:
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      print("Current Time =", current_time)

      # request the images
      # r = requests.get(GET_ALL_IMAGES_API, headers={'Authorization': 'Bearer ' + IMAGES_API_KEY})
      # imagesData = r.json()
      imagesData = {'success': True, 'data': [{'id': 16, 'uploaded_date': '2024-06-01T00:50:01.559781+00:00', 'bucket_location': 'images/DSCF7668.jpg', 'uploaded_by': 'anon', 'storage_id': '2bdfbb18-f0bb-43ec-a54a-72bb48c52fc3'}, {'id': 17, 'uploaded_date': '2024-06-03T16:55:41.252596+00:00', 'bucket_location': 'images/qrcode_www.yelp.com.png', 'uploaded_by': 'anon', 'storage_id': '99440625-4d2b-4b4e-afc6-a0f5301c9fe9'}]}

      if imagesData['success']:
        for image in imagesData['data']:
          image_bucket_location = image['bucket_location']
          image_name = os.path.basename(image_bucket_location)
          image_url = IMAGES_BUCKET_BASE + '/' + image_bucket_location

          print('saving image ' + image_name)

          # save the image to our images directory
          img_data = requests.get(image_url).content
          with open(IMAGES_DIR + '/' + image_name, 'wb') as handler:
              handler.write(img_data)

    except Exception as e:
      print('Error---')
      print(e)
    
    time.sleep(image_dowload_rate)
except KeyboardInterrupt:
  sys.exit(0)
