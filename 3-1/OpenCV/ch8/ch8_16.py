import numpy as np
import cv2

def contain_pts(p, p1, p2):
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

def draw_rect(img):
    rois = [(p-small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y + h, x:x + w]
        val = np.full(roi.shape, 80, np.uint8)
        cv2.add(roi, val, roi)
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)
    return img

def warp(img):
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (400, 350), cv2.INTER_CUBIC)
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param):
    global check
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, p in enumerate(pts1):
            p1, p2 = p - small, p + small
            if contain_pts((x, y), p1, p2):
                check = i

    if event == cv2.EVENT_LBUTTONUP:
        check = -1

    if check >= 0:
        pts1[check] = (x, y)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise Exception("카메라를 열 수 없습니다.")

small = np.array((12, 12))
check = -1
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])

cv2.namedWindow("select rect")
cv2.setMouseCallback("select rect", onMouse)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_copy = draw_rect(np.copy(frame))
    cv2.imshow("select rect", img_copy)
    warp(np.copy(frame))

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()