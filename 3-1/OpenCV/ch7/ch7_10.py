import cv2
import numpy as np

def filter_channel(image_channel, mask):
    rows, cols = image_channel.shape[:2]
    dst = np.zeros((rows, cols), dtype=np.float32)
    ycenter, xcenter = mask.shape[0] // 2, mask.shape[1] // 2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image_channel[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst.astype(np.uint8)

image = cv2.imread('filter_sharpen.jpg')
blur_mask = np.ones((3, 3), np.float32) / 9

blurred_image = np.zeros_like(image)
for i in range(3):
    blurred_image[:, :, i] = filter_channel(image[:, :, i], blur_mask)

sharpen_mask = np.array([[0, -1, 0],
                          [-1, 5, -1],
                          [0, -1, 0]], dtype=np.float32)

sharpened_image = np.zeros_like(image)
for i in range(3):
    sharpened_image[:, :, i] = filter_channel(image[:, :, i], sharpen_mask)

blurred_and_sharpened_image = cv2.filter2D(blurred_image, -1, sharpen_mask)

cv2_blurred = cv2.filter2D(image, -1, blur_mask)

cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('plus', blurred_and_sharpened_image)
cv2.imshow('bluring OpenCV', cv2_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()