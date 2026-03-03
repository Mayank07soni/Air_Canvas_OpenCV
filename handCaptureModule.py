import cv2 as cv
import numpy as np
import mediapipe as mp
import time

class handDetector():
    #making a constructor to initialize value 
    def __init__(self,mode=False,max_num_hands=2, min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.mode=mode
        self.max_num_hands= max_num_hands
        self.min_detection_confidence= min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.mpDraw=mp.solutions.drawing_utils  #self represent class object
        self.tipIds=[4,8,12,16,20]
        self.handType="Right"

    def findHands(self,img,draw=True):
        ImgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results= self.hands.process(ImgRGB)

        if self.results.multi_hand_landmarks:
            if self.results.multi_handedness:
                self.handType = self.results.multi_handedness[0].classification[0].label

            for handLms in self.results.multi_hand_landmarks:
                if draw:
                   self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self,img,max_num_hands=0,draw=True):
        
        self.lmList=[]

        if self.results.multi_hand_landmarks:  
            myHand=self.results.multi_hand_landmarks[max_num_hands]     
            for id,lm in enumerate(myHand.landmark):
                        h,w,c=img.shape
                        cx,cy=int(lm.x*w),int(lm.y*h)
                        self.lmList.append([id,cx,cy])
                               
        return self.lmList

    def fingerUp(self):
        fingers=[]
        if len(self.lmList) == 0:
            return fingers
    
        if self.handType == "Right":
            if self.lmList[self.tipIds[0]][1]<self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        elif self.handType == "Left":
            if self.lmList[self.tipIds[0]][1]>self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)


        for id in range(1,5):
             if self.lmList[self.tipIds[id]][2]<self.lmList[self.tipIds[id]-2][2]:
                  fingers.append(1)

             else :
                  fingers.append(0)    

        return fingers
            
                
def main():
    cap =cv.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img=cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        cv.imshow("Image",img)
        cv.waitKey(1)

if __name__ == "__main__": #if file is directly running 
    main()   