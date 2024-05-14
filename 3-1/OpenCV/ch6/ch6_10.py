import numpy as np
import cv2

# float32 타입으로 이미지 생성
image1 = np.zeros((50, 512), np.float32)
image2 = np.zeros((50, 512), np.float32)

rows, cols = image1.shape[:2]

# 각 이미지에 대해 회색조를 점진적으로 짙어지게 함
for i in range(rows):
    for j in range(cols):
        # 정규화는 구글링 한 값으로 넣음
        image1.itemset((i, j), j / 512)  # 0.0에서 1.0 사이로 정규화
        image2.itemset((i, j), (j // 20) * 10 / 255)  # 0.0에서 1.0 사이로 정규화

# 이미지 표시
cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
