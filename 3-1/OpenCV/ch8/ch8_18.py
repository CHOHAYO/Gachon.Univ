import numpy as np
import cv2

def draw_bar(img, pt, w, bars):
    pt = np.array(pt, np.int32)
    for bar in bars:
        (x, y), h = pt, w * 6
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)
        if bar == 0:
            y = y + w * 3 - w // 4
            h = w // 2
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)
        pt += (int(w * 1.5), 0)

c = 200
r, sr, c2, c4 = c // 2, c // 4, c * 2, c * 4
img = np.full((c4, c4, 3), 255, np.uint8)
blue, red = (255, 0, 0), (0, 0, 255)

cv2.ellipse(img, (c2, c2), (r, r), 0, 0, 180, blue, -1)
cv2.ellipse(img, (c2, c2), (r, r), 180, 0, 180, red, -1)
cv2.ellipse(img, (c2 + r - sr, c2), (sr, sr), 180, 0, 180, blue, -1)
cv2.ellipse(img, (c2 - sr, c2), (sr, sr), 0, 0, 180, red, -1)

left = (c2 - c * (18+8)/24, c2-sr)
right = (c2 + c * (18+0)/24, c2-sr)
draw_bar(img, left, c//12, (1, 1, 1))
draw_bar(img, right, c//12, (0, 0, 0))

cv2.imshow("image", img)
cv2.waitKey(0)