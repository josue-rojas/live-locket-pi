import sqlite3

IMAGES_DB = "images.db"

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
