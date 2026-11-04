import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

import numpy as np
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
result = cv2.dilate(binary, np.ones((5,5), np.uint8), iterations=1)
cv2.imshow("Original Binary", binary); cv2.imshow("Dilation", result)
cv2.waitKey(0); cv2.destroyAllWindows()
