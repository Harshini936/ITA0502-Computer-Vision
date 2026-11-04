import cv2
from tkinter import Tk,filedialog
root=Tk(); root.withdraw()
path=filedialog.askopenfilename(title="Select a video",filetypes=[("Videos","*.mp4 *.avi *.mov *.mkv")])
if not path: raise SystemExit("No video selected.")
cap=cv2.VideoCapture(path); frames=[]
while True:
    ok,frame=cap.read()
    if not ok: break
    frames.append(frame)
cap.release()
if not frames: raise SystemExit("No frames found.")
h,w=frames[0].shape[:2]
fps=10
writer=cv2.VideoWriter("reversed_slow_motion.avi",cv2.VideoWriter_fourcc(*"XVID"),fps,(w,h))
for frame in reversed(frames):
    writer.write(frame); writer.write(frame)  # repeat each frame for slower playback
writer.release()
print("Saved reversed_slow_motion.avi")
