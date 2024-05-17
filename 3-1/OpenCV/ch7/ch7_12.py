import cv2
import numpy as np

def laplacian_edge_detection(image):
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])

    laplacian_result = cv2.filter2D(image, -1, laplacian_kernel)

    return laplacian_result

def DoG_edge_detection(image):
    gaussian_blur_1 = cv2.GaussianBlur(image, (5, 5), 0)
    gaussian_blur_2 = cv2.GaussianBlur(image, (9, 9), 0)

    DoG_result = gaussian_blur_1 - gaussian_blur_2

    return DoG_result

image = cv2.imread('filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)

laplacian_result = laplacian_edge_detection(image)

DoG_result = DoG_edge_detection(image)

cv2.imshow('Original Image', image)
cv2.imshow('Laplacian', laplacian_result)
cv2.imshow('DoG', DoG_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
