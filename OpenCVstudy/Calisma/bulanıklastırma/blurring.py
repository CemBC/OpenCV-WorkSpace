import cv2
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

#blurring
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()


#Ortalama bulanıklaştırma yöntemi


dst2 = cv2.blur(img, ksize   = (3,3)) #ksize = kernel size
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Mean Blurred")
plt.show()

#Gaussian blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7) #eğer sigmaY yi belirtmezsen sigmaX = sigmaY
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gaussian")
plt.show()

#Median Blur
mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Median Blur")
plt.show()



def gaussian_noise(image):
    row, col , ch = img.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5
    
    gauss = np.random.normal(mean , sigma ,(row, col , ch))
    gauss = gauss.reshape(row , col , ch)
    noisy = image + gauss
    return noisy

#to normalize
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255  # maksimum sınır 255/225 = 1 olur minimum sınır 0/255 = 0 olur
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Normalized"),plt.show()


gaussianNoisyImage = gaussian_noise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gaussian Noised"),plt.show()

    
gb = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX= 7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gaussian Noised with Gauss Blur"),plt.show()
 

def salt_pepper_noise(image):
    row,col ,ch = image.shape
    s_vs_p = 0.5
    amount =  0.004
    noisy = np.copy(image)
    
    #salt / beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0 ,i -1 , int(num_salt)) for i in image.shape]
    
    noisy[tuple(coords)] = 1
    
    
    #pepper / siyah
    num_pepper = np.ceil(amount * image.size * 1-s_vs_p)
    coords = [np.random.randint(0 , i -1  , int(num_pepper)) for i in image.shape]
    
    noisy[tuple(coords)] = 0
    
    return noisy

spImage = salt_pepper_noise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("Salt Pepper Noisy"),plt.show()
    
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3) 
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("Salt and Pepper with Median Blur"),plt.show()
    























