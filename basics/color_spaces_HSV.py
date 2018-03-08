#color spacing using HSV
#color ranges for hsv H(0-179),S(0-255),V(0-255)
import cv2
import numpy

image=cv2.imread(r'../images/moana1.jpg')

#converting RGB image to HSV
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#displaying the image in hsv
cv2.imshow('HSV_IMAGE',hsv_image)
cv2.imshow('Hue channel',hsv_image[:,:,0])
cv2.imshow('Saturation channel',hsv_image[:,:,1])
cv2.imshow('Value channel',hsv_image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()
