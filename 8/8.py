import cv2

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

img_laplace = cv2.Laplacian(img, cv2.CV_8U, ksize=5)    # laplace 필터 적용

cv2.imshow('laplace', img_laplace)  # 이미지 미리보기
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('D:\image\san1_laplace.jpg', img_laplace)   # 이미지 저장
