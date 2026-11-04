import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

# Simple watch detector demo: use a Haar cascade if available, otherwise show the selected image.
# Haar cascades do not include a standard watch model; this displays the watch image for visual inspection.
cv2.putText(image, "Watch object input", (15,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
cv2.imshow("Watch Recognition Input", image)
print("Note: OpenCV has no built-in general watch detector. A trained watch model is needed for reliable recognition.")
cv2.waitKey(0); cv2.destroyAllWindows()
