import cv2

img = cv2.imread("Lenna_(test_image).png", 1)

print("Resim boyutu = " , img.shape)

cv2.imshow("orijinal" , img)

imgResized = cv2.resize(img , (800,800))
print("Resized image shape " , imgResized.shape)

cv2.imshow("resized", imgResized)

imgCropped = img[   :500:600]
cv2.imshow("cropped",imgCropped)
k = cv2.waitKey(0) & 0xFF

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: 
        cv2.destroyAllWindows()
        break    