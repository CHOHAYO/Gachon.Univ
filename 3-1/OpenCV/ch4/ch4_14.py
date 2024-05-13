#연습문제 14번
import numpy as np
import cv2

# 마우스 콜백 함수 정의
def onMouse(event, x, y, flags, param):
    global title, pt  # 전역 변수 사용 선언

    # 마우스 왼쪽 버튼 클릭 이벤트 처리
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:  # 시작점이 설정되지 않았으면
            pt = (x, y)  # 시작점 설정
        else:  # 시작점이 이미 설정되어 있으면
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)  # 사각형 그리기
            cv2.imshow(title, image)  # 이미지 다시 표시
            pt = (-1, -1)  # 시작점 초기화

    # 마우스 중간 버튼 클릭 이벤트 처리
    elif event == cv2.EVENT_MBUTTONDOWN:
        if pt[0] < 0:  # 시작점이 설정되지 않았으면
            pt  = (x, y)  # 시작점 설정
        else:  # 시작점이 이미 설정되어 있으면
            dx, dy = pt[0] - x, pt[1] - y  # 거리 계산
            radius = int(np.sqrt(dx*dx + dy*dy))  # 반지름 계산
            cv2.ellipse(image, pt, (200, radius), 0, 0, 360, (0, 165, 255), 2)  # 타원 그리기
            cv2.imshow(title, image)  # 이미지 다시 표시
            pt = (-1, -1)  # 시작점 초기화

    # 마우스 오른쪽 버튼 클릭 이벤트 처리
    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:  # 시작점이 설정되지 않았으면
            pt = (x, y)  # 시작점 설정
        else:  # 시작점이 이미 설정되어 있으면
            dx, dy = pt[0] - x, pt[1] - y  # 거리 계산
            radius = int(np.sqrt(dx*dx + dy*dy))  # 반지름 계산
            cv2.circle(image, pt, radius, (0, 0, 255), 2)  # 원 그리기
            cv2.imshow(title, image)  # 이미지 다시 표시
            pt = (-1, -1)  # 시작점 초기화

# 이미지 생성 및 초기화
image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)  # 시작점 초기화
title = "Draw Event"  # 창 제목 설정

cv2.imshow(title, image)  # 창에 이미지 표시
cv2.setMouseCallback(title, onMouse)  # 마우스 콜백 함수 등록

cv2.waitKey(0)  # 키 입력 대기
