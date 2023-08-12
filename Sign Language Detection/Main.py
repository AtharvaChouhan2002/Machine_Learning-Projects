import math 
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from cvzone.ClassificationModule import Classifier
import time


import os



cap=cv2.VideoCapture(0)
detector=HandDetector(maxHands=2)
Alphabetsclassifier=Classifier("ML Model\Alphabets\keras_model.h5","ML Model\Alphabets\labels.txt")
NumberClassifier=Classifier(r"ML Model\Numerals\keras_model.h5",r"ML Model\Numerals\labels.txt")

offset=20
imgsize=350

counter=0

stack=[0]
l=["A","B","C","D,1","E","F","G","H","I","J","K,2","L","O","P","Q","R","U","W,3","X","Y","Z"]
Numbers=["6","7"]


while True:
    success,img=cap.read()
    imgOutput=img.copy()
    hands,img=detector.findHands(img)
    if hands:
        if len(hands)==1:
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
                prediction,index=Alphabetsclassifier.getPrediction(imgwhite)
                
                
            
            else:
                k=imgsize/w
                Calculatedheight=math.ceil(k*h)
                imgresize=cv2.resize(imgcrop,(imgsize,Calculatedheight))
                imgresizeShape=imgresize.shape
                Hgap=math.ceil((imgsize-Calculatedheight)/2)
                imgwhite[Hgap:Calculatedheight+Hgap]=imgresize
                prediction,index=Alphabetsclassifier.getPrediction(imgwhite)


            cv2.rectangle(imgOutput,(x,y),(x+w,y+h),(255,0,255),4)
            cv2.putText(imgOutput,l[index],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
            cv2.imshow("CroppedImage",imgcrop)
            
        
        if len(hands)==2:
            try:
                hand1=hands[0]
                hand2=hands[1]
                x1,y1,w1,h1=hand1["bbox"]
                x2,y2,w2,h2=hand2["bbox"]
                imgwhite=np.ones((imgsize,imgsize,3),np.uint8)*255
                imgcrop=img[y1-offset:y2+max(h1,h2)+offset,x1-offset:x2+w1+w2+offset]
                Ymin=min(y1,y2)
                Ymax=max(y1,y2)
                Xmin=min(x1,x2)
                Xmax=max(x1,x2)
                Hmax=max(h1,h2)
                Wmax=max(w1,w2)
                prediction,index=NumberClassifier.getPrediction(imgcrop)
                cv2.putText(imgOutput,Numbers[index],(Xmin,Ymin),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)           
                cv2.imshow("CroppedImage",imgcrop)
            except:
                pass
            


            
            





            
        


    cv2.imshow("Image",imgOutput)
    key=cv2.waitKey(1)
  
