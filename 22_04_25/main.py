import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([179, 255, 30])
    mask = cv.inRange(hsv, lower_black, upper_black)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF #waitkey is escape key
    if k == 27:
        break   
