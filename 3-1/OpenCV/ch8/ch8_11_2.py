import cv2
import numpy as np

image = cv2.imread('rotate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("이미지를 로드하는 데 실패했습니다.")

rotation_angle = 30
center = (100, 100)
rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()