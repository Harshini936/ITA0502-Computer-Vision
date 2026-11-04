import cv2
from tkinter import Tk, filedialog
root = Tk(); root.withdraw()
path = filedialog.askopenfilename(title="Select an image", filetypes=[("Images","*.jpg *.jpeg *.png *.bmp")])
if not path: raise SystemExit("No image selected.")
image = cv2.imread(path)
if image is None: raise SystemExit("Could not read image.")

face=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
smile=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
for (x,y,w,h) in face.detectMultiScale(gray,1.3,5):
    roi=gray[y:y+h,x:x+w]; color=image[y:y+h,x:x+w]
    for (sx,sy,sw,sh) in smile.detectMultiScale(roi,1.7,20):
        cv2.rectangle(color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
cv2.imshow("Smile Detection",image); cv2.waitKey(0); cv2.destroyAllWindows()
