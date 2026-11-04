import cv2
from tkinter import Tk, filedialog
root=Tk(); root.withdraw()
path=filedialog.askopenfilename(title="Select a video", filetypes=[("Videos","*.mp4 *.avi *.mov *.mkv")])
if not path: raise SystemExit("No video selected.")
cap=cv2.VideoCapture(path)
bg=cv2.createBackgroundSubtractorMOG2()
while True:
    ok, frame=cap.read()
    if not ok: break
    mask=bg.apply(frame)
    mask=cv2.threshold(mask, 220, 255, cv2.THRESH_BINARY)[1]
    contours,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        x,y,w,h=cv2.boundingRect(c)
        if w>45 and h>25 and w*h>1200:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"Moving object",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
    cv2.imshow("Vehicle / Moving Object Detection",frame)
    if cv2.waitKey(30)&0xFF==ord('q'): break
cap.release(); cv2.destroyAllWindows()
print("This basic background-subtraction demo marks moving objects; it is not a trained vehicle classifier.")
