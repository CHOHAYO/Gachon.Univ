import cv2

def gaussian_blur(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

def median_blur(image):
    blurred_image = cv2.medianBlur(image, 5)
    return blurred_image

def bilateral_filter(image):
    blurred_image = cv2.bilateralFilter(image, 9, 75, 75)
    return blurred_image

image = cv2.imread('filter_sharpen.jpg')

gaussian_blurred = gaussian_blur(image)
median_blurred = median_blur(image)
bilateral_blurred = bilateral_filter(image)

cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blurred Image', gaussian_blurred)
cv2.imshow('Median Blurred Image', median_blurred)
cv2.imshow('Bilateral Blurred Image', bilateral_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
