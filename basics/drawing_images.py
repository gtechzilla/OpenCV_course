import cv2
import numpy as np

#creating a black square image
#we use numpy zeros function
#dimensions are 512 by 512,the 3 is for the color dimension
image = np.zeros((512,512,3),np.uint8)

#for a black and white images
#for a black and white image we remove the color dimension
img_bw = np.zeros((512,512),np.uint8)

cv2.imshow("Black rectange(colored)",image)
cv2.imshow("Black rectange(black&white)",img_bw)

#Drawing a line over our black square
#we use opencv's line function
#the arguments are as follows
'''we start with the image,start co-ordinate of the line,
end co-ordinate,color of the line(g,g,r),thickness of the line'''
cv2.line(image,(0,0),(200,512),(240,230,0),5)
cv2.imshow('our_line',image)

#drawing a rectangle
#we use the rectangle cv2 function
#arguments are the same as with the line function
#we drew it on our black and white image
cv2.rectangle(img_bw,(0,0),(100,100),(128,240,0),5)
cv2.imshow('Our green rectange',img_bw)

#what about circles
#we use cv2 circle function
img_circle=np.zeros((300,300,3),np.uint8)
img_circle2=np.zeros((300,300,3),np.uint8)
'''its arguments are (image,center co-ordinate,radius,color,fill)'''
cv2.circle(img_circle,(150,150),90,(0,0,255),1)
cv2.imshow('image with circle',img_circle)
#filled circle
cv2.circle(img_circle2,(150,150),90,(0,0,255),-1)
cv2.imshow('image with circle filled',img_circle2)

#lets draw a polygon
img_polygon=np.zeros((400,600,3),np.uint8)
#now we define four points
points=np.array([[10,50],[300,50],[80,200],[60,400]],np.int32)
#reshaping the points into the form required by polylines
points=points.reshape(-1,1,2)
cv2.polylines(img_polygon,[points],True,(0,255,0),3)
cv2.imshow('polygon',img_polygon)

#we can add text to our images
#we use opencv putText function
'''arguments are in the following order
(image,text to display,bottom left starting point,font,font size,color,thickness)
'''
#please check the documentation to know the various fonts opencv supports
image_text=np.zeros((512,512),np.uint8)
cv2.putText(image_text,'hey ppl',(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
cv2.imshow('image_text',image_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
