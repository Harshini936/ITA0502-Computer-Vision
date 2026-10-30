import cv2
import numpy as np

img = cv2.imread("sample.jpg")

rows, cols = img.shape[:2]

pts1 = np.float32([
    [100, 100],
    [700, 100],
    [100, 500]
])

pts2 = np.float32([
    [150, 150],
    [650, 100],
    [150, 450]
])

matrix = cv2.getAffineTransform(pts1, pts2)

result = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
