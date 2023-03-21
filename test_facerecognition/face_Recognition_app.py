
import cv2
import sqlite3
import numpy as np
import face_recognition as faceRegLib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# app = Flask(__name__)
# db = SQLAlchemy(app)

# load from database file  

def Convert(temp , temp2):
    filename = f"{temp}.jpg"
    with open(filename,"wb") as f:
        img = f.write(temp2)
        print(" Successfully decoded ")
    f.close()
    return filename

with sqlite3.connect("Instance/sample_img.db") as conn:
    cur = conn.cursor()
    val = cur.execute(" SELECT * FROM Image_Table ")
    for x in val:
        name = x[0]
        img_Db = Convert(name, x[1])
    conn.commit()
    print(" Successfully Img Retrived ")
    cur.close()
conn.close()

# First Image

#original_img=faceRegLib.load_image_file('1.jpg')

original_img=faceRegLib.load_image_file(img_Db)
original_img_rgb = cv2.cvtColor(original_img,cv2.COLOR_BGR2RGB)
copy = original_img_rgb.copy()
face = faceRegLib.face_locations(original_img_rgb)[0] 
cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (0,0,255), 2)
cv2.imshow('Orginal rgb', copy)
cv2.imshow('ElonMask Orginal ',original_img_rgb)
cv2.waitKey(0)

# Original Image from local 

# Second Image 

demo_img_bgr = faceRegLib.load_image_file('test.jpg')
emo_img_rgb = cv2.cvtColor(demo_img_bgr,cv2.COLOR_BGR2RGB)
original_face = faceRegLib.face_locations(demo_img_bgr)[0] 
demo_train_encode = faceRegLib.face_encodings(demo_img_bgr)[0]
cv2.imshow('Duplicate rgb', emo_img_rgb)
cv2.rectangle(emo_img_rgb, (face[3], face[0]),(face[1], face[2]), (0,0,255), 6)
cv2.imshow('ElonMusk Duplicate', emo_img_rgb)
cv2.waitKey(0)

# compare Faces of Encodings 

demo_encode = faceRegLib.face_encodings(original_img_rgb)[0] 
print(faceRegLib.compare_faces([demo_train_encode],demo_encode))

