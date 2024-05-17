import cv2
import numpy as np

def median_filter(image, kernel_size):
    height, width = image.shape[:2]
    filtered_image = np.zeros_like(image)
    radius = kernel_size // 2

    for y in range(height):
        for x in range(width):
            values = []
            for ky in range(-radius, radius + 1):
                for kx in range(-radius, radius + 1):
                    if 0 <= y + ky < height and 0 <= x + kx < width:
                        values.append(image[y + ky, x + kx])

            filtered_image[y, x] = np.median(values)

    return filtered_image

image = cv2.imread('filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)

kernel_size = 3
filtered_image = median_filter(image, kernel_size)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image (Median Filter)', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()