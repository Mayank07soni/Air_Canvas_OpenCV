import cv2 as cv
import numpy as np
import mediapipe as mp
import time

cap =cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
#use only RGB IMAGE 
mpDraw=mp.solutions.drawing_utils

while True:
    success, img=cap.read()
    ImgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results= hands.process(ImgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h) #lm.x,y are in normalized form converting to screen size
                if id==8:
                    cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cv.imshow("Image",img)
    cv.waitKey(1)