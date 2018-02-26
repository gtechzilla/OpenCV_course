# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:31:23 2018

@author: gtechzilla
"""

import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("harman",frame)
    cv2.waitKey(1) & 0XFF
cap.release()
cv2.destroyAllWindows()