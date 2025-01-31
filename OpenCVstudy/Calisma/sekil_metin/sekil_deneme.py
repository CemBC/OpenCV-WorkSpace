import cv2

import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)



cv2.line(img , (100,100) , (195,195) , (0 , 255 , 0), 5)  #BGR = (255, 0 , 0 ) blue
cv2.rectangle(img , (200,200) ,(400,400) , (255 , 0 , 0 ) ,5     ) 
cv2.circle(img , (300,300) , 95 ,(0,0,255) ,cv2.FILLED)
cv2.putText(img, "Nugget", (250,300), cv2.FONT_HERSHEY_COMPLEX, 1 , (255, 255,255))
#üst üste binerken sıralama önemli

cv2.imshow("Cizgi", img)



while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: 
        cv2.destroyAllWindows()
        break