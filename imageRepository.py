import sqlite3
from constants import IMAGES_DB

def get_random_image():
    with sqlite3.connect(IMAGES_DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT 1;")
        return cur.fetchone()

def get_all_images():
    with sqlite3.connect(IMAGES_DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM images")
        images = cur.fetchall()
        return images

def get_start_image():
    with sqlite3.connect(IMAGES_DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM images WHERE ID = 0")
        return cur.fetchone()

def insert_image(image):
    with sqlite3.connect(IMAGES_DB) as con:
        sql = '''INSERT OR IGNORE INTO images(id, uploaded_date, uploaded_by, filename, storage_id, bucket_location)
                 VALUES(?, ?, ?, ?, ?, ?)'''
        cur = con.cursor()
        cur.execute(sql, (image['id'], image['uploaded_date'], image['uploaded_by'], 
                          image['filename'], image['storage_id'], image['bucket_location']))
        con.commit()
        return cur.lastrowid
