import cv2
import numpy as np

#to create histogram plots we use matplotlib
from matplotlib import pyplot as plt

image =cv2.imread(r'../images/moana1.jpg')

#describing feartures for our histogram such as size,scale etc
#calcHist function assigns our histogram properties
#first argument is the source of our image,it has to be in square brackets
#2nd argument is for the color channel,0 is greyscale.For colored images,u may use 0,1 or 2 but in brackets to get blue,green or red channel respectively
#3rd argument is the mask,u may use none to show a histogram for the full image,a histogram for a specific region,you create a mask for it
#4th argument is the histogram size,its in binary count,for full size use 256
#5th argument is range,it normally [0,256] i.e x-axis
histogram = cv2.calcHist([image],[0],None,[256],[0,256])

#to plot the histogram,we first flatten our image using ravel,i.e makes it a 1 dimensional array
plt.hist(image.ravel(),256,[0,256])
plt.show()
