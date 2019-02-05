import cv2
import numpy as np

image1 = cv2.imread("twoimg.png")
image2 = cv2.imread("fourimg.png")

difference = cv2.subtract(image1,image2)

result = not np.any(difference)

if result is True:
    print "Images are same"
else:
    cv2.imwrite("result.png", difference)
    print "images are not same"