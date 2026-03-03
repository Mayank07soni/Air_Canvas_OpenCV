import cv2 as cv
import os 
import numpy as np
import handCaptureModule as htm

folderPath="header"
myList=os.listdir(folderPath)
overlayList=[]

for imPath in myList:
    image=cv.imread(f'{folderPath}/{imPath}')
    image = cv.resize(image, (1280,125)) 
    overlayList.append(image)

header=overlayList[0]
drawColor=(255,0,255)
brushThickness=10

cap =cv.VideoCapture(0)
cap.set(3,1280) #width 
cap.set(4,1280)#height

detector=htm.handDetector(0.85)
xp,yp=0,0
imgCanvas= None

while True:
     success, img=cap.read()
     img =cv.flip(img,1)
     if imgCanvas is None:
       imgCanvas = np.zeros_like(img)
     img =detector.findHands(img)
     lmList =detector.findPosition(img,draw=False)

     if len(lmList)!=0:
          
          x1,y1=lmList[8][1:]  #[8,x1,y1]
          x2,y2=lmList[12][1:]

          fingers=detector.fingerUp()     
          
          #selection mode 
          if fingers[1] and fingers[2]:
               xp,yp=0,0
               cv.rectangle(img, (x1,y1-50),(x2,y2+50), (255,0,255),cv.FILLED)
               
               if y1<125:
                    if 65<=x1<290:
                         header=overlayList[0]
                         drawColor=(1,1,233)
                    elif 290<x1<=515:  
                         header=overlayList[1]
                         drawColor= (213,122,36) 
                    elif 515<x1<=740:  
                         header=overlayList[2]
                         drawColor=(0,255,255)
                    elif 740<x1<=965:  
                         header=overlayList[3] 
                         drawColor=(0,125,12)
                    elif 965<x1<=1190:  
                         header=overlayList[4] 
                         drawColor=(0,0,0)    


          if fingers[1] and not fingers[2]:
               cv.circle(img, (x1,y1),25, (255,0,255),cv.FILLED)
                
               if xp==0 and yp==0:
                    xp,yp=x1,y1

               if drawColor==(0,0,0):  
                brushThickness=100  
               else:
                    brushThickness=10
                    
               cv.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
               cv.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
              
               xp,yp=x1,y1

     imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)  
     _,imgInv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)   
     imgInv=cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR) 
     img =cv.bitwise_and(img,imgInv)
     img=cv.bitwise_or(img,imgCanvas)

     img[0:125,0:1280]=header #replace top the height with 0-125 and width with 0-1280
     
     cv.imshow("Image",img)

     cv.waitKey(1)
