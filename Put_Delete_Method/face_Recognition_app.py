import cv2
import numpy as np
import face_recognition as faceRegLib

demo_img_bgr = faceRegLib.load_image_file('1.jpg')
emo_img_rgb = cv2.cvtColor(demo_img_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow('bgr', emo_img_rgb)
cv2.imshow('rgb', demo_img_bgr)
cv2.waitKey(0)

original_img=faceRegLib.load_image_file('1.jpg')
original_img_rgb = cv2.cvtColor(original_img,cv2.COLOR_BGR2RGB)

face = faceRegLib.face_locations(original_img_rgb)[0] 
copy = original_img_rgb.copy()

cv2.rectangle(copy, (face[3], face[0]),(face[1], face[2]), (0,0,255), 2)
cv2.imshow('copy', copy)
cv2.imshow('Original',original_img_rgb)
cv2.waitKey(0)

img_sample = faceRegLib.load_image_file('1.jpg')
img_sample_rgb = cv2.cvtColor(img_sample,cv2.COLOR_BGR2RGB)
original_face = faceRegLib.face_locations(img_sample)[0] 
demo_train_encode = faceRegLib.face_encodings(img_sample)[0]
demo = faceRegLib.load_image_file('1.jpg')
demo = cv2.cvtColor(demo, cv2.COLOR_BGR2RGB)
demo_encode = faceRegLib.face_encodings(demo)[0] 
print(faceRegLib.compare_faces([demo_train_encode],demo_encode))
cv2.rectangle(img_sample_rgb, (face[3], face[0]),(face[1], face[2]), (0,0,255), 6)
cv2.imshow('OBAMA', img_sample_rgb)
cv2.waitKey(0)