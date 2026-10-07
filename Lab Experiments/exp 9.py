import cv2

img = cv2.imread("sample6.jpg")

bigger = cv2.resize(img, (800, 600))
smaller = cv2.resize(img, (300, 200))

cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
