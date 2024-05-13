import numpy as np, cv2

image1 = cv2.imread("images/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백으로 영상 읽기
image2 = cv2.imread("images/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None: raise Exception("영상파일 읽기 오류")

dif_img1 = cv2.subtract(image1, image2)                               # 차분 영상
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))           # 음수 결과 보존

abs_dif1 = np.absolute(dif_img2).astype('uint8')
abs_dif2 = cv2.absdiff(image1, image2)                                # 절대값 차분계산

x, y, w, h = 100, 150, 7, 3

print(f"(dif_img1(roi) uint8) = \n{dif_img1[y:y+h, x:x+w]}")          # 광산 영상 결과 출력확인
print(f"(dif_img2(roi) int16) = \n{dif_img2[y:y+h, x:x+w]}")
print(f"(abs_dif1(roi)) = \n{abs_dif1[y:y+h, x:x+w]}")
print(f"(abs_dif2(roi)) = \n{abs_dif2[y:y+h, x:x+w]}")

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']     # 윈도우 제목 리스트

for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)
