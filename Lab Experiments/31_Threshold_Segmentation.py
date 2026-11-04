import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
threshold_value= int(input("Enter threshold value (0-255): "))
_, segmented=cv2.threshold(gray,threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow("Original",image); cv2.imshow("Segmented",segmented)
cv2.waitKey(0); cv2.destroyAllWindows()
