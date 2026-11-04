import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

import numpy as np\nhsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower=np.array([0,0,0]); upper=np.array([180,80,100])
mask=cv2.inRange(hsv,lower,upper)
background_removed=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Original",image); cv2.imshow("Selected dark-color regions",background_removed)
cv2.waitKey(0); cv2.destroyAllWindows()
