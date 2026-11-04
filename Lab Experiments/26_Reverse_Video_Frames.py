import cv2
from tkinter import Tk, filedialog
root=Tk(); root.withdraw()
path=filedialog.askopenfilename(title="Select a video", filetypes=[("Videos","*.mp4 *.avi *.mov *.mkv")])
if not path: raise SystemExit("No video selected.")
cap=cv2.VideoCapture(path); frames=[]
while True:
    ok, frame=cap.read()
    if not ok: break
    frames.append(frame)
cap.release()
if not frames: raise SystemExit("No frames found.")
h,w=frames[0].shape[:2]
writer=cv2.VideoWriter("reversed_video.avi", cv2.VideoWriter_fourcc(*"XVID"), 20, (w,h))
for frame in reversed(frames): writer.write(frame)
writer.release()
print("Saved reversed_video.avi")
