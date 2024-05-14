import cv2
import numpy as np
import matplotlib.pyplot as plt # type: ignore

image = cv2.imread('images/add1.jpg', cv2.IMREAD_GRAYSCALE)

# 수직 투영 히스토그램을 계산
vertical_projection = cv2.reduce(image, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

# 수평 투영 히스토그램을 계산
horizontal_projection = cv2.reduce(image, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32S)

# 결과 투영 히스토그램을 시각화
# 수직 투영 히스토그램
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Vertical Projection')
plt.plot(vertical_projection[0])
plt.xlabel('Columns')
plt.ylabel('Sum of pixel values')

# 수평 투영 히스토그램
plt.subplot(1, 2, 2)
plt.title('Horizontal Projection')
plt.plot(horizontal_projection)
plt.xlabel('Rows')
plt.ylabel('Sum of pixel values')

# 플롯을 화면에 보여줌
plt.tight_layout()
plt.show()
