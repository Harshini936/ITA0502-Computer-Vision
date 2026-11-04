import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=cascade.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces: cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
print("Number of faces:",len(faces))
cv2.imshow("Face Count",image); cv2.waitKey(0); cv2.destroyAllWindows()
