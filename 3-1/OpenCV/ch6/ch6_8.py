import cv2
import numpy as np

image1 = cv2.imread('images/add1.jpg')
image2 = cv2.imread('images/add2.jpg')

# 이미지의 크기를 확인하고, 합성할 중간 이미지의 크기 설정
# 여기서는 두 이미지가 같은 크기라고 가정
if image1.shape != image2.shape:
    raise ValueError("Images must be the same size for blending.")

# cv2.addWeighted()를 사용하여 두 이미지를 합성
alpha = 0.5  # 합성 이미지의 가중치를 설정
blended = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)

# 캔버스(배경)생성. 너비는 두 이미지와 합성 이미지의 너비 합임
height = image1.shape[0]
canvas_width = image1.shape[1] * 3  # 세 개의 이미지 너비
canvas = np.zeros((height, canvas_width, 3), dtype=np.uint8)

# 첫 번째 이미지를 캔버스의 왼쪽에 배치
canvas[:, :image1.shape[1]] = image1

# 합성된 이미지를 캔버스의 중앙에 배치
mid_start = image1.shape[1]
mid_end = mid_start + blended.shape[1]
canvas[:, mid_start:mid_end] = blended

# 두 번째 이미지를 캔버스의 오른쪽에 배치
canvas[:, mid_end:mid_end+image2.shape[1]] = image2

cv2.imshow('dst', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
