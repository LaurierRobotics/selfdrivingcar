# packages 
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/laithadi/Desktop/Robotics/Project/selfdrivingcar/laneDetectionModule/roadImage.jpg')

def threshold(img):

    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([80, 0, 0])
    upperWhite = np.array([255, 160, 255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)

    return maskWhite

def laneDetection(img):
    
    imgthres = threshold(img)

    return imgthres


i = laneDetection(image) 

cv2.imshow('image', i)
cv2.waitKey(0) 