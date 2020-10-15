# packages 
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt


# function for lane detection 
def laneDetection(img):

    # show og img 
    print(img.shape)
    cv2.imshow('OG', img)
    cv2.waitKey(0)

    # turn the image into gray scale
    gr_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show the gray img
    print(gr_img.shape) 
    cv2.imshow('GRAY', gr_img)
    cv2.waitKey(0)

    # blur the img 
    blr_img = cv2.GaussianBlur(gr_img, (7,7), 0)
    # show blur img
    print(blr_img.shape) 
    cv2.imshow('BLUR', blr_img)
    cv2.waitKey(0)

    # canny the img for edge detection 
    thr_low = 10 
    thr_high = 200 
    can_img = cv2.Canny(blr_img, thr_low, thr_high)
    # show canny img 
    cv2.imshow('CANNY', can_img)
    cv2.waitKey(0)

    # region of interest 
    vertices = np.array([[(0, 324), (0, 289), (220, 186), (315, 186), (449, 324)]], dtype=np.int32)
    mask = np.zeros_like(gr_img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(gr_img, mask)
    masked_img = cv2.bitwise_and(can_img, mask)
    # show  
    cv2.imshow("MASKED", masked_img)
    cv2.waitKey(0)

    # hough lines detection 
    rho = 2 
    theta = np.pi / 180 
    thres = 40 
    min_line_len = 100
    max_line_len = 50
    lines = cv2.HoughLinesP(masked_img, rho, theta, thres, np.array([]), min_line_len, max_line_len)

    # create an empty black img 
    line_image = np.zeros((masked_img.shape[0], masked_img.shape[1], 3), dtype=np.uint8)

    cv2.imshow("LINES", line_image)
    cv2.waitKey(0)

    for line in lines:
        # print(line)
        for x1,y1,x2,y2 in line:
            cv2.line(line_image, (x1,y1), (x2,y2), [255, 0, 0], 20)

    cv2.imshow("LINES1", line_image)
    cv2.waitKey(0)

    # print(lines)

    # putting it together 
    alpha = 1
    beta = 1 
    gamma = 0 

    print(can_img.shape)
    print(line_image.shape)

    image_with_lines = cv2.addWeighted(img, alpha, line_image, beta, gamma)

    return image_with_lines





# getting the image 
image = cv2.imread('/Users/laithadi/Desktop/Robotics/Project/selfdrivingcar/laneDetectionModule/roadImage.jpg')

finalimg = laneDetection(image)

cv2.imshow('img', finalimg)
cv2.waitKey(0)



