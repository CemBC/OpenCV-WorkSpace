import cv2
import numpy as np

img = cv2.imread("kart.png")
cv2.imshow("A", img)

width = 400
height = 500

pts1 = np.float32([[200,1] , [1,472] , [540,150] , [338,617]])
pts2= np.float32([[0,0] , [0, height] , [width,0] , [width , height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)


imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("B",imgOutput)
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    else:
        continue