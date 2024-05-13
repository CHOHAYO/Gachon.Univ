#연습문제 18번
import numpy as np
import cv2

# 색상 정의
red, blue, white = (0, 0, 255), (255, 0, 0), (255, 255, 255)

# 흰색 배경 이미지 생성
image = np.full((400, 600, 3), white, np.uint8)

# 태극 문양 중앙 지점 계산
pt1 = (int(image.shape[1]/2), int(image.shape[0]/2))

# 태극 문양의 크기 설정 (반지름의 길이)
size1 = (int(image.shape[1]/8), int(image.shape[1]/8)) # 반지름 = 가로 길이의 1/8

# 상단의 반원 그리기 (빨간색)
cv2.ellipse(image, pt1, size1, 0, 0, -180, red, -1)

# 하단의 반원 그리기 (파란색)
cv2.ellipse(image, pt1, size1, 0, 0, 180, blue, -1)

# 작은 반원의 중심을 위한 좌표 계산
# 왼쪽 작은 반원의 중심
pt2 = (int(image.shape[1]/2) - int(size1[1]/2), int(image.shape[0]/2))
# 오른쪽 작은 반원의 중심
pt3 = (int(image.shape[1]/2) + int(size1[1]/2), int(image.shape[0]/2))

# 작은 반원의 크기 설정 (반지름의 길이)
size2 = (int(image.shape[1]/16), int(image.shape[1]/16)) # 반지름 = 가로 길이의 1/16

# 왼쪽 작은 빨간 반원 그리기
cv2.ellipse(image, pt2, size2, 0, 0, 180, red, -1)

# 오른쪽 작은 파란 반원 그리기
cv2.ellipse(image, pt3, size2, 0, 0, -180, blue, -1)

# 결과 이미지 표시
cv2.imshow("Taegeuk", image)

# 키 입력 대기 (키를 누를 때까지 무한 대기)
cv2.waitKey()
