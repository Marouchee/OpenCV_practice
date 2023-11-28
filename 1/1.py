import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) #파일 읽어오기(흑백)
plt.hist(img.ravel(), 256, [0,256]) #히스토그램 그래프표시
plt.show()
