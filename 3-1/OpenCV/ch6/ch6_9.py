import cv2
import numpy as np

# 트랙바 콜백 함수
def update_blend(x):
    alpha = cv2.getTrackbarPos('image1', 'dst') / 100
    beta = cv2.getTrackbarPos('image2', 'dst') / 100
    blended = cv2.addWeighted(image1, alpha, image2, beta, 0)
    canvas[:, image1.shape[1]:image1.shape[1]*2] = blended
    cv2.imshow('dst', canvas)

image1 = cv2.imread('images/add1.jpg')
image2 = cv2.imread('images/add2.jpg')

# 이미지의 크기를 확인하고, 합성할 중간 이미지의 크기를 설정
if image1.shape != image2.shape:
    raise ValueError("Images must be the same size for blending.")

# 캔버스(배경) 이미지를 생성
height, width = image1.shape[:2]
canvas_width = width * 3  # 세 개의 이미지 너비
canvas = np.zeros((height, canvas_width, 3), dtype=np.uint8)

# 첫 번째 이미지와 두 번째 이미지를 배치
canvas[:, :width] = image1
canvas[:, width*2:width*3] = image2

# 윈도우 생성 및 트랙바 추가
cv2.namedWindow('dst')
cv2.createTrackbar('image1', 'dst', 50, 100, update_blend)
cv2.createTrackbar('image2', 'dst', 50, 100, update_blend)

# 초기 블렌딩 비율로 합성된 이미지를 중앙에 배치
update_blend(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
