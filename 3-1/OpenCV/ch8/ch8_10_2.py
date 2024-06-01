import cv2
import numpy as np

def translate_image_opencv(image, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return translated_image

image = cv2.imread('filter_sharpen.jpg')

tx, ty = 50, 60

opencv_translated_image = translate_image_opencv(image, tx, ty)

cv2.imshow('Original Image', image)
cv2.imshow('OpenCV Translated Image', opencv_translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
