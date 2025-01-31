import cv2
import numpy as np
img = cv2.imread("Lenna_(test_image).png" )
cv2.imshow("Orijinal" , img)

hor = np.hstack( (img,img))
cv2.imshow("Horizontal", hor)

ver = np.vstack((img,img))
cv2.imshow("Vertical", img)

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    else:
        continue