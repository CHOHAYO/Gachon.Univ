#연습문제 16번
import numpy as np
import cv2

# 카메라(웹캠)를 열어서 capture 객체에 저장
capture = cv2.VideoCapture(0)

# 카메라가 제대로 연결되었는지 확인
if capture.isOpened() == False:
    raise Exception("카메라 연결 안 됨")

# 비디오 스트림의 프레임 크기 및 속성 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)  # 자동 초점 비활성화
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)  # 밝기를 0으로 설정

title = "test_16"
cv2.namedWindow(title)  # 디스플레이 창 생성

while True:
    ret, frame = capture.read()  # 프레임 읽기
    if not ret:
        break  # 프레임을 읽지 못하면 반복 종료

    if cv2.waitKey(1) == 27:  # ESC 키를 누르면 루프 종료
        break

    # 프레임으로부터 BGR 채널 분리
    blue, green, red = cv2.split(frame)

    # 밝기를 증가시킬 영역에 50을 더함 (오류 수정 필요)
    # 오류 수정: green 채널에 직접 값을 더하고 결과를 다시 저장
    green[100:300, 200:300] = cv2.add(green[100:300, 200:300], 50)

    # 수정된 채널을 다시 합쳐서 최종 프레임 생성
    frame = cv2.merge([blue, green, red])

    # 지정한 영역에 빨간색 사각형 그리기
    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)

    # 최종 프레임 디스플레이
    cv2.imshow(title, frame)

# 자원 해제
capture.release()
