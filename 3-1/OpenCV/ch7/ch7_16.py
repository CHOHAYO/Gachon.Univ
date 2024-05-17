import numpy as np
import cv2

def morphology(img, mask, operation):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None:
        mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)
            if operation == 'erode':
                dst[i, j] = 255 if (cnt == cv2.countNonZero(mask)) else 0
            elif operation == 'dilate':
                dst[i, j] = 0 if (cnt == 0) else 255
    return dst

image = cv2.imread("morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
mask = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype("uint8")

eroded_image = morphology(th_img, mask, 'erode')
dilated_image = morphology(th_img, mask, 'dilate')

cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
