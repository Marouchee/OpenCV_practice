import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)
img_br = cv2.add(img, 50)   # 50만큼 밝게 처리
img_dr = cv2.add(img, -50)  # 50만큼 어둡게 처리

cv2.imshow('br', img_br) # 밝게 처리된 사진 미리보기
cv2.waitKey()   # 키보드 입력을 기다리는 함수. 아무키나 누를시 다음 코드로 넘어감.
cv2.destroyAllWindows() # 모든 창 닫기
cv2.imshow('dr', img_dr) # 어둡게 처리된 사진 미리보기
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_br.jpg',img_br)  # 밝게 처리된 사진 저장
cv2.imwrite('D:\image\san1_dr.jpg',img_dr)  # 어둡게 처리된 사진 저장

plt.hist(img_br.ravel(), 256, [0,256]) # 밝게 처리한 이미지 히스토그램 그래프 표시
plt.show()
plt.hist(img_dr.ravel(), 256, [0,256]) # 어둡게 처리한 이미지 히스토그램 그래프 표시
plt.show()
