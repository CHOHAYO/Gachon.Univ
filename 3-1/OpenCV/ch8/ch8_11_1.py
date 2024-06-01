import numpy as np
import cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1] - 1: x = img.shape[1] - 2
    if y >= img.shape[0] - 1: y = img.shape[0] - 2

    P1 = float(img[y, x])
    P2 = float(img[y, x + 1])
    P3 = float(img[y + 1, x])
    P4 = float(img[y + 1, x + 1])

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)

def rotate(img, degree, center):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = j - center[0], i - center[1]
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x += center[0]
            y += center[1]
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, [x, y])
    return dst

image = cv2.imread('rotate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("이미지를 로드하는 데 실패했습니다.")

center = (100, 100)
rotation_angle = 30
rotated_image = rotate(image, rotation_angle, center)

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()