import cv2
import numpy as np

image = cv2.imread("test.jpg", 0)
blur_image = cv2.GaussianBlur(image, (5,5), 1)

cv2.imshow('home', blur_image)

cv2.waitKey(0)

cv2.destroyAllWindows()