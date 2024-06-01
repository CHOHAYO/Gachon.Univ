import numpy as np
import math
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

def rotate(img, degree):
    if len(img.shape) == 3:
        channels = cv2.split(img)
        rotated_channels = [rotate_channel(channel, degree) for channel in channels]
        return cv2.merge(rotated_channels)
    else:
        return rotate_channel(img, degree)

def rotate_channel(channel, degree):
    dst = np.zeros(channel.shape, channel.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(channel.shape[0]):
        for j in range(channel.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin
            if contain((y, x), channel.shape):
                dst[i, j] = bilinear_value(channel, [x, y])
    return dst

def rotate_pt(img, degree, pt):
    if len(img.shape) == 3:
        channels = cv2.split(img)
        rotated_channels = [rotate_pt_channel(channel, degree, pt) for channel in channels]
        return cv2.merge(rotated_channels)
    else:
        return rotate_pt_channel(img, degree, pt)

def rotate_pt_channel(channel, degree, pt):
    dst = np.zeros(channel.shape, channel.dtype)
    radian = (degree / 180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(channel.shape[0]):
        for j in range(channel.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), channel.shape):
                dst[i, j] = bilinear_value(channel, (x, y))
    return dst

image = cv2.imread('rotate.jpg')
if image is None: raise Exception("영상 파일 읽기 에러")

center = (100, 100)
dst1 = rotate(image, 30)
dst2 = rotate_pt(image, 30, center)

cv2.imshow("image", image)
cv2.imshow("dst1-rotated on org", dst1)
cv2.imshow("dst2-rotated on center", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()