import cv2, numpy as np
width=int(input("Enter image width: ")); height=int(input("Enter image height: "))
image=np.ones((height,width,3),dtype=np.uint8)*255
box_w=max(1,width//10); box_h=max(1,height//10)
image[0:box_h,0:box_w]=(0,0,0)                 # black
image[0:box_h,width-box_w:width]=(255,0,0)    # blue (BGR)
image[height-box_h:height,0:box_w]=(0,255,0)  # green
image[height-box_h:height,width-box_w:width]=(0,0,255) # red
cv2.imshow("Four Corner Boxes",image); cv2.waitKey(0); cv2.destroyAllWindows()
