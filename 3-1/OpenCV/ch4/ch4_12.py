#연습문제 12번
import numpy as np
import cv2

def onChange(value):  # 트랙바의 위치(값)를 인자로 받습니다.
    global image, title
    image[:] = value  # 이미지의 모든 픽셀 값을 현재 트랙바의 값으로 설정합니다.
    cv2.imshow(title, image)  # 변경된 이미지를 다시 표시합니다.

image = np.zeros((300, 500), np.uint8)  # 검은색 이미지 생성
title = 'Trackbar Event'
cv2.imshow(title, image)
cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)  # 트랙바 생성

while True:
    key = cv2.waitKey(100)  # 변경된 부분
    if key == 27:  # ESC 키를 누르면 루프 탈출
        break
    if key == 2424832:  # 왼쪽 화살표 키
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value - 1)
    elif key == 2555904:  # 오른쪽 화살표 키
        value = cv2.getTrackbarPos('Brightness', title)
        cv2.setTrackbarPos('Brightness', title, value + 1)

cv2.destroyAllWindows()
