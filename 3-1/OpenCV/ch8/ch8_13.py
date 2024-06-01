import cv2
import numpy as np
import math

drawing = False
start_point = None
end_point = None
image = None

def draw_line(event, x, y, flags, param):
    global drawing, start_point, end_point, image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = None
        print(f"시작지점: {start_point}")

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            img_copy = image.copy()
            cv2.line(img_copy, start_point, end_point, (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        print(f"완료지점: {end_point}")
        img_copy = image.copy()
        cv2.line(img_copy, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow('image', img_copy)
        calculate_length_and_slope(start_point, end_point)

def calculate_length_and_slope(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.sqrt(dx**2 + dy**2)
    slope = math.degrees(math.atan2(dy, dx))
    print(f"길이: {length}")
    print(f"기울기: {slope} ")

image = np.ones((500, 500, 3), np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_line)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()