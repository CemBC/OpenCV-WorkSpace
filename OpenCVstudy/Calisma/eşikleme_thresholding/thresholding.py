import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img , cmap= "gray")
plt.axis("off")
plt.show()

#eşikleme
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)
#_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thresh_img , cmap = "gray")
plt.axis("off")
plt.show()


thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11 , 8)
plt.figure()
plt.imshow(thresh_img2 , cmap = "gray")
plt.axis("off")
plt.show()