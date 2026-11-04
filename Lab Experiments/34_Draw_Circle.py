import cv2, numpy as np
width=int(input("Enter image width: ")); height=int(input("Enter image height: "))
image=np.ones((height,width,3),dtype=np.uint8)*255
radius=max(1,min(width,height)//4)
cv2.circle(image,(width//2,height//2),radius,(0,0,255),3)
cv2.imshow("Circle",image); cv2.waitKey(0); cv2.destroyAllWindows()
