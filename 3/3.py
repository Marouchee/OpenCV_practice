import cv2

img = cv2.imread('D:\image\san1.jpg', cv2.IMREAD_GRAYSCALE) # 파일 읽어 오기(흑백)

ret, img_bin_30 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY) # 이진화
cv2.imshow('bin', img_bin_30)    # Threshold값 30부터 순서대로 출력, 저장
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_30.jpg', img_bin_30)

ret, img_bin_60 = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_60)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_60.jpg', img_bin_60)

ret, img_bin_90 = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_90)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_90.jpg', img_bin_90)

ret, img_bin_120 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_120)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_120.jpg', img_bin_120)

ret, img_bin_150 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_150)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_150.jpg', img_bin_150)

ret, img_bin_180 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_180)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_180.jpg', img_bin_180)

ret, img_bin_210 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_210)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_210.jpg', img_bin_210)

ret, img_bin_240 = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', img_bin_240)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('D:\image\san1_bin_240.jpg', img_bin_240)
