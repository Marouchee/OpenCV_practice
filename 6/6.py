import cv2

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

img_smoothing = cv2.blur(img, (5, 5))   # smoothing(Averaging) 처리
cv2.imshow('smoothing', img_smoothing)  # 이미지 미리보기
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_smoothing.jpg', img_smoothing)   # 이미지 저장
