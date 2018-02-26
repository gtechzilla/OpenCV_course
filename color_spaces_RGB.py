import cv2
import numpy as np

image = cv2.imread(r'C:\Users\gtechzilla\Documents\cv\images\moana.jpg')

#BGR values for the first pixel
'''B, G, R = image[0,0]
print("The colors below are values of blue,red and green for the first pixel")
print (B, G, R)
print("\n")

#converting the image to greyscale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#shape method shows dimensions of the greyscale image
#GREYSCALE IMAGES HAVE 2 dimensions
print("grey scale images only have 2 dimensions:x and y")
print (grey_image.shape)

#IN GREYSCALE IMAGES,EACH DIMENSION HAS ONE COLOR values
#BGR(COLORED IMAGES) HAVE 3 VALUES
#COLOR FOR THE FIRST pixel
print("There color value is only an expression of the degree of grey")
print(grey_image[0,0])'''

'''
#INDIVIDUAL COLOR CHANNELS IN RGB IMAGES

#We use the openCV's split function to split an image to individual color spaces
B,G,R =cv2.split(image)
#show image dimensions
print (image.shape)
#displays windows with individual filters
#image will be greyscale since we only have one dimension for color
cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)

#we can recombine the color spaces to have the original image
#we use openCV's merge function
merged_image=cv2.merge([B,G,R])
cv2.imshow('Merged_image',merged_image)

#we can further manipulate individual colors
#to modify Blue

merged_image=cv2.merge([B+100,G,R])
cv2.imshow("Modified with blue color",merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#how to get an image with only one color space of RGB
#We use the openCV's split function to split colors to individual color spaces
B,G,R =cv2.split(image)

#first we create a matrix of zeros
#the matrix has three dimensions h,x,q

zeros=np.zeros(image.shape[:2],dtype="uint8")

cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
