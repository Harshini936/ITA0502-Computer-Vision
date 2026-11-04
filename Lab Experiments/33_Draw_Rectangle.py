import cv2, numpy as np
width=int(input("Enter image width: ")); height=int(input("Enter image height: "))
image=np.ones((height,width,3),dtype=np.uint8)*255
cv2.rectangle(image,(width//4,height//4),(3*width//4,3*height//4),(255,0,0),3)
cv2.imshow("Rectangle",image); cv2.waitKey(0); cv2.destroyAllWindows()
