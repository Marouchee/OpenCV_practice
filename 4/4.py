import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

img_str = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)  # 이미지 스트레칭
cv2.imshow('stretching', img_str)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_stretching.jpg', img_str) # 이미지 저장

plt.hist(img_str.ravel(), 256, [0,256])  # 히스토그램 출력
plt.show()
