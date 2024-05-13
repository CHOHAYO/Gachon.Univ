#연습문제 8번
import numpy as np
import cv2

mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

title1, title2 = 'win_mode1', 'win_mode2'

h, w = mat1.shape

cv2.imshow(title1, mat1)
cv2.imshow(title2, mat2)
cv2.moveWindow(title1, 0, 0)
cv2.moveWindow(title2, w, h)
cv2.waitKey(0)
cv2.destroyAllWindows()