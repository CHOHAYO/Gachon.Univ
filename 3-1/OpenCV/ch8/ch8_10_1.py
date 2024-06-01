import cv2
import numpy as np


def translate_image_manual(image, tx, ty):
    rows, cols, _ = image.shape
    translated_image = np.zeros_like(image)

    for y in range(rows):
        for x in range(cols):
            new_x = x + tx
            new_y = y + ty
            if 0 <= new_x < cols and 0 <= new_y < rows:
                translated_image[new_y, new_x] = image[y, x]

    return translated_image


image = cv2.imread('filter_sharpen.jpg')


tx, ty = 50, 60

manual_translated_image = translate_image_manual(image, tx, ty)

cv2.imshow('Original Image', image)
cv2.imshow('Manual Translated Image', manual_translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
