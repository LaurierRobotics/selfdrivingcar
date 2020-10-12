# packages 
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

image = cv2.imread('/Users/laithadi/Desktop/Robotics/Project/selfdrivingcar/laneDetectionModule/roadImage.jpg')

def threshold(img):

    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lowerThreshold = 200
    upperThreshold = 254
    maskWhite = cv2.inRange(imgHsv, lowerThreshold, upperThreshold)

    return maskWhite

def laneDetection(img):
    
    imgthres = threshold(img)

    # cv2.imshow('thres', imgthres)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)

    

    return imgthres


lane = laneDetection(image)

cv2.imshow('thres', lane)
cv2.imshow('img', image)
cv2.waitKey(0)