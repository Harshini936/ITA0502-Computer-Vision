import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

x, y, w, h = 80, 60, min(220, image.shape[1]-80), min(160, image.shape[0]-60)
roi = image[y:y+h, x:x+w].copy()
result = image.copy()
# Paste a copy of the selected ROI at the top-right when space permits
px = max(0, image.shape[1]-w-10); py = 10
result[py:py+h, px:px+w] = roi
cv2.imshow("Original", image); cv2.imshow("Cropped ROI", roi); cv2.imshow("ROI copied and pasted", result)
cv2.waitKey(0); cv2.destroyAllWindows()
