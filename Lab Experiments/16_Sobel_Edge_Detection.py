import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.addWeighted(cv2.convertScaleAbs(gx), 0.5, cv2.convertScaleAbs(gy), 0.5, 0))
cv2.imshow("Original", image); cv2.imshow("Sobel Edges", sobel)
cv2.waitKey(0); cv2.destroyAllWindows()
