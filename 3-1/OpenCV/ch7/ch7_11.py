import cv2
import numpy as np

def apply_mask(image, mask):
    rows, cols = image.shape
    mask_size = mask.shape[0]
    half_size = mask_size // 2

    result = np.zeros((rows - mask_size + 1, cols - mask_size + 1))

    for i in range(half_size, rows - half_size):
        for j in range(half_size, cols - half_size):
            roi = image[i - half_size:i + half_size + 1, j - half_size:j + half_size + 1]
            result[i - half_size, j - half_size] = np.sum(roi * mask)

    return result.astype(np.uint8)

def roberts_mask():
    return np.array([[1, 0, 0],
                     [0, -1, 0],
                     [0, 0, 0]])

def prewitt_mask():
    return np.array([[-1, 0, 1],
                     [-1, 0, 1],
                     [-1, 0, 1]])

def sobel_mask():
    return np.array([[-1, 0, 1],
                     [-2, 0, 2],
                     [-1, 0, 1]])

image = cv2.imread('filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)

roberts_result = apply_mask(image, roberts_mask())
prewitt_result = apply_mask(image, prewitt_mask())
sobel_result = apply_mask(image, sobel_mask())

cv2.imshow('Original Image', image)
cv2.imshow('Roberts Result', roberts_result)
cv2.imshow('Prewitt Result', prewitt_result)
cv2.imshow('Sobel Result', sobel_result)
cv2.waitKey(0)
cv2.destroyAllWindows()