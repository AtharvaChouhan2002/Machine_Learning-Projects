import math 
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time

cap=cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)
offset=20
imgsize=350
folder="rough"
counter=0





while True:
    success,img=cap.read()
    hands,img=detector.findHands(img)
    if hands:
        hand=hands[0]
        x,y,w,h=hand["bbox"]
        imgwhite=np.ones((imgsize,imgsize,3),np.uint8)*255
        imgcrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
        
        

        aspectratio=h/w

        if aspectratio>1:
            k=imgsize/h
            CalculatedWidth=math.ceil(k*w)
            imgresize=cv2.resize(imgcrop,(CalculatedWidth,imgsize))
            imgresizeShape=imgresize.shape
            Wgap=math.ceil((imgsize-CalculatedWidth)/2)
            imgwhite[:,Wgap:CalculatedWidth+Wgap]=imgresize

        else:
            k=imgsize/w
            Calculatedheight=math.ceil(k*h)
            imgresize=cv2.resize(imgcrop,(imgsize,Calculatedheight))
            imgresizeShape=imgresize.shape
            Hgap=math.ceil((imgsize-Calculatedheight)/2)
            imgwhite[Hgap:Calculatedheight+Hgap]=imgresize




        cv2.imshow("CroppedImage",imgcrop)
        cv2.imshow("imgwhite",imgwhite)


    cv2.imshow("Image",img)
    key=cv2.waitKey(1)
    if key==ord("s"):
        counter+=1
        cv2.imwrite(f"{folder}/Image_{time.time()}.jpg",imgwhite)
        print(counter)

