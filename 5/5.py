import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

img_equalization = cv2.equalizeHist(img)  # 이미지 평활화
cv2.imshow('equalization', img_equalization)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_equalization.jpg', img_equalization) # 이미지 저장

plt.hist(img_equalization.ravel(), 256, [0,256])  # 히스토그램 출력
plt.show()
