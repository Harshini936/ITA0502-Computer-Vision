import cv2
import numpy as np

img = cv2.imread("sample.jpg")

width = 600
height = 400

pts1 = np.float32([
    [100, 100],
    [700, 100],
    [700, 500],
    [100, 500]
])

pts2 = np.float32([
    [0, 0],
    [width, 0],
    [width, height],
    [0, height]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
