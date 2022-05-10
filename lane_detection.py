import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('lane_vgt.mp4')

while cap.isOpened():
    
    ret,frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    kernel = np.ones((2,2), np.uint8)

    roi = frame[170: ,:]

    lower_green= np.array([120, 120, 120])
    upper_green = np.array([255, 255, 255])

    lower_yellow = np.array([0, 127, 220])
    upper_yellow = np.array([255, 255, 255])
    
    mask1 = cv.inRange(roi, lower_green, upper_green)
    mask2 = cv.inRange(roi, lower_yellow, upper_yellow)
    mask_inv2 = cv.bitwise_not(mask2)
    
    mask = cv.bitwise_and(mask1, mask_inv2)
    res = cv.bitwise_and(roi, roi, mask = mask)
    
    gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    
    ret, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
    
    median = cv.medianBlur(thresh, 3)
    
    erosion = cv.erode(median,kernel,iterations = 1)

    edges = cv.Canny(erosion, 5, 200)
    
    while True:
        lines = cv.HoughLinesP(edges, 5, np.pi/180, 100, minLineLength = 90, maxLineGap = 80)

        if lines is None: 
            print("Cannot detect lines")
            break

        for line in lines:
             x1,y1,x2,y2 = line[0]
             cv.line(roi,(x1,y1),(x2,y2),(255,0,255),2)

        break

    cv.imshow("frame", frame)

    # cv.imshow("res", res)
    # cv.imshow("thresh", thresh)
    # cv.imshow("median", median)
    # cv.imshow("Erosion", erosion)
    # cv.imshow("canny", edges)
    # cv.imshow("erode", erosion)
    
    if cv.waitKey(2) == ord('q'):    
        break

cap.release()
cv.destroyAllWindows()
