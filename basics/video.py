# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:31:23 2018

@author: gtechzilla
"""

import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(1) & 0XFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
