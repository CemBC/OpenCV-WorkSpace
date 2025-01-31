import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("datai_team.jpg" , 0)
plt.figure(),plt.imshow(img , cmap ="gray"),plt.axis("off"),plt.title("Orijinal"),plt.show()

#erozyon
kernel = np.ones((5,5) , dtype = np.uint8)
result = cv2.erode(img , kernel , iterations= 1)

plt.figure(),plt.imshow(result , cmap = "gray"),plt.axis("off"),plt.title("Erozyon"),plt.show()

#genişletme dilation
result = cv2.dilate(img , kernel , iterations= 1)

plt.figure(),plt.imshow(result , cmap = "gray"),plt.axis("off"),plt.title("Genişletme"),plt.show()

#white noise
whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise , cmap = "gray"),plt.axis("off"),plt.title("White Noise"),plt.show()

noise_img = whiteNoise + img
plt.figure(),plt.imshow(noise_img , cmap = "gray"),plt.axis("off"),plt.title("Image with White Noise"),plt.show()


#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(),plt.imshow(opening , cmap = "gray"),plt.axis("off"),plt.title("Acilma"),plt.show()


#black noise
blackNoise = np.random.randint(low = 0, high = 2, size = img.shape[:2])
blackNoise = blackNoise*-255
black_noise_img = blackNoise + img
plt.figure(),plt.imshow(black_noise_img, cmap = "gray"),plt.axis("off"),plt.title("Black Noise"),plt.show()

black_noise_img[black_noise_img <= -245] = 0
plt.figure(),plt.imshow(black_noise_img, cmap = "gray"),plt.axis("off"),plt.title("Image with Black Noise"),plt.show()

#kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(),plt.imshow(closing,cmap = "gray"),plt.axis("off"),plt.title("Kapatma"),plt.show()



#gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(),plt.imshow(gradient,cmap = "gray"),plt.axis("off"),plt.title("Gradient"),plt.show()


























