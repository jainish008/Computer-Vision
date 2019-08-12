import cv2
import numpy as np
#First Input the image
image = cv2.imread("old.jpg")
#below is parameters for setting brightness 
alpha = 2
beta = 50

#Result 
result=cv2.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), 0, beta)

#Now to show the image
cv2.imwrite("new.jpg", result)
