import numpy as np
import cv2

no = 1

while True:
    fname = "images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    if image is None:
        print(str(no) + "번 영상 파일이 없습니다.")
        break

    mask = np.ones((5, 17), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)

    _, th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)

    key = cv2.waitKey(0)

    if key == 27:
        break
    elif key == 2490368:
        no += 1
    elif key == 2621440:
        no -= 1
    else:
        print("지원하지 않는 키입니다.")