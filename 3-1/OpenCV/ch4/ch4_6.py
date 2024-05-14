#연습문제 6번
import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 100

title = 'Position'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(title, 500, 600)

cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()