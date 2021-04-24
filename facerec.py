import cv2 
import numpy as np
import argparse
import os 
import dlib
# from imageai.Detection import VideoObjectDetection

# CLASSES = ['Leg', 'Arm', 'Face', 'Hand', 'Chest']

# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# print("[INFO] loading model:...")


imcap = cv2.VideoCapture(0)

imcap.set(3, 640)
imcap.set(4, 480)

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detector = dlib.get_frontal_face_detector()

# img_one = cv2.imread('test.png')
# color_gray = cv2.cvtColor(img_one, cv2.COLOR_BGR2GRAY)

while True: 
    success, img = imcap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

    faces,_,_ = detector.run(image = imgGray, upsample_num_times = 0,
                            adjust_threshold = 0.0)

    # for (x,y,w,h) in faces: 
    #     imgGray = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
    
    cv2.imshow('face_detect', imgGray)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

imcap.release()
cv2.destroyWindow('face_detect')


# for (x,y,w,h) in faces:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#    roi_gray = color_gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]

#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
