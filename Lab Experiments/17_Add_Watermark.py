import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

watermark = "MY WATERMARK"
output = image.copy()
cv2.putText(output, watermark, (20, image.shape[0]-25), cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("Watermarked Image", output)
cv2.imwrite("watermarked_output.jpg", output)
print("Saved as watermarked_output.jpg in the current working folder.")
cv2.waitKey(0); cv2.destroyAllWindows()
