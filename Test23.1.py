import cv2
import numpy as np




while True:

    cap = cv2.imread('rich.jpg')
    gray = cv2.GaussianBlur(cap, (5, 5), 0)
    thresh = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)[1]
    thresh[np.where((thresh != [255, 255, 255]).any(axis=2))] = [0, 0, 0]
    thresh = cv2.dilate(thresh, None, iterations=2)




    thresh = cv2.cvtColor(thresh, cv2.COLOR_RGB2GRAY)
    (__, cnts, hierarchy) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for c in cnts:

        area = cv2.contourArea(c)

        if area > 0:
            cv2.drawContours(cap, [c], -1, (0, 0, 255), 2)
    #

    cv2.imshow("Frame", cap)
    cv2.imshow("thes", thresh)

    key = cv2.waitKey(1)
    if key == 27:
        break
