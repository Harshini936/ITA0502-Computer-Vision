import cv2

# Read the image
img = cv2.imread("sample.jpg")

# Create kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Apply erosion
eroded = cv2.erode(img, kernel)

# Display original image
cv2.imshow("Original Image", img)

# Display eroded image
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
