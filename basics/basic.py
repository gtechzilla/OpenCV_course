import cv2
img=cv2.imread(r'..\images\moana.jpg',0)
cv2.imshow('moana',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
