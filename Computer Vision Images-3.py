import numpy as np
import matplotlib as plt
import cv2

image_1 = cv2.imread("club.jpg")

gamma = 0.5

image_2 = np.power(image_1, gamma)

gamma = 1

image_3 = np.power(image_1, gamma)


cv2.imshow("original", image_1)
cv2.imshow("gamma_1", image_2)
cv2.imshow("gamma_2", image_3)
cv2.waitKey(0)
cv2.destroyAllWindows()