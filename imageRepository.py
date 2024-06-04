import sqlite3
from constants import IMAGES_DB

def getRandomImage():
  con = sqlite3.connect(IMAGES_DB)
  cur = con.cursor()
  res = cur.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT 1;")
  
  return res.fetchone()

def getAllImages(): 
  if len(images):
      return images
  con = sqlite3.connect(IMAGES_DB)
  cur = con.cursor()
  res = cur.execute("SELECT * FROM images")
  images = res.fetchall()

  return images

def getStartImage():
    con = sqlite3.connect(IMAGES_DB)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM images where ID = 0")

    return res.fetchone()

# how do I insert this data {'id': 16, 'uploaded_date': '2024-06-01T00:50:01.559781+00:00', 'bucket_location': 'images/DSCF7668.jpg', 'uploaded_by': 'anon', 'storage_id': '2bdfbb18-f0bb-43ec-a54a-72bb48c52fc3'} into sqlite using python. I have table with 
def insetImage(image):
  con = sqlite3.connect(IMAGES_DB)
  sql = '''INSERT OR IGNORE INTO images(id, uploaded_date, uploaded_by, filename, storage_id, bucket_location)
  VALUES(?, ?, ?, ?, ?, ?)'''
  cur = con.cursor()
  cur.execute(sql, image)
  con.commit() 

  return cur.lastrowid
