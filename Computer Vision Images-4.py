import numpy as np
import cv2
# Reading our image and displaying it
image = cv2.imread('club.jpg')
# Let's try with 7 x 7 kernel to get a more blurred image
kernel_7x7 = np.ones((7, 7), np.float32) / 49
blurred2 = cv2.filter2D(image, -1, kernel_7x7)
kernel_9x9 = np.ones((9, 9), np.float32) / 81
# We apply the filter and display the image
blurred_3 = cv2.filter2D(image, -1, kernel_9x9)
cv2.imshow('Original Image', image)
cv2.imshow('7x7 Kernel Blurring', blurred2)
cv2.imshow('9x9 Kernel Blurring', blurred_3)
cv2.waitKey(0)
cv2.destroyAllWindows()