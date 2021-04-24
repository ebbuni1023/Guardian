import cv2 
import numpy as np
import argparse
import os 
import dlib
import math

BLINK_RATIO_THRESHOLD = 5.7

# from imageai.Detection import VideoObjectDetection

# CLASSES = ['Leg', 'Arm', 'Face', 'Hand', 'Chest']

# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# print("[INFO] loading model:...")

def midpoint(point1 ,point2):
    return (point1.x + point2.x)/2,(point1.y + point2.y)/2

def euclidean_distance(point1 , point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_blink_ratio(eye_points, facial_landmarks):
    
    #loading all the required points
    corner_left  = (facial_landmarks.part(eye_points[0]).x, 
                    facial_landmarks.part(eye_points[0]).y)
    corner_right = (facial_landmarks.part(eye_points[3]).x, 
                    facial_landmarks.part(eye_points[3]).y)
    
    center_top    = midpoint(facial_landmarks.part(eye_points[1]), 
                             facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), 
                             facial_landmarks.part(eye_points[4]))

    #calculating distance
    horizontal_length = euclidean_distance(corner_left,corner_right)
    vertical_length = euclidean_distance(center_top,center_bottom)

    ratio = horizontal_length / vertical_length

    return ratio

imcap = cv2.VideoCapture(0)

imcap.set(3, 640)
imcap.set(4, 480)

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("face_eyes.dat")

left_eye_landmarks = [36, 37, 38, 39, 40, 41]
right_eye_landmarks = [42, 43, 44, 45, 46, 47]

# img_one = cv2.imread('test.png')
# color_gray = cv2.cvtColor(img_one, cv2.COLOR_BGR2GRAY)

while True: 
    success, img = imcap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

    faces,_,_ = detector.run(image = imgGray, upsample_num_times = 0, adjust_threshold = 0.0)


    # for (x,y,w,h) in faces: 
    #     imgGray = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

    for face in faces:
        
        landmarks = predictor(imgGray, face)

        #-----Step 5: Calculating blink ratio for one eye-----
        left_eye_ratio  = get_blink_ratio(left_eye_landmarks, landmarks)
        right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
        blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2

        if blink_ratio > BLINK_RATIO_THRESHOLD:
            #Blink detected! Do Something!
            cv2.putText(imgGray,"BLINKING",(10,50), cv2.FONT_HERSHEY_SIMPLEX,
                        2,(255,255,255),2,cv2.LINE_AA)
    
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
