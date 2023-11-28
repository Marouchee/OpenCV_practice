import cv2

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

img_scharrX = cv2.Sobel(img, -1, 1, 0, ksize=cv2.FILTER_SCHARR) # Gradient(scharr) 순서대로 dx,dy 처리
img_scharrY = cv2.Sobel(img, -1, 0, 1, ksize=-1)
img_scharr = img_scharrX + img_scharrY  # dx, dy 합성

cv2.imshow('scharr', img_scharrX)  # 이미지 미리보기
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('scharr', img_scharrY)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('scharr', img_scharr)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('D:\image\san1_gradient_x.jpg', img_scharrX)   # 이미지 저장
cv2.imwrite('D:\image\san1_gradient_y.jpg', img_scharrY)
cv2.imwrite('D:\image\san1_gradient.jpg', img_scharr)
