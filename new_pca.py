import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv


print("Enter image path..../home/abc/pic.jpg")
path=input()

img=Image.open(path)
print("Actual Image:",end=" ")
print(img.mode)
gray=cv.imread(path,0)

img=np.asarray(img,dtype=np.uint8)
original=img
r,c,d=img.shape
img=np.reshape(img,(r*c,3))
img2=np.transpose(img)

img3=np.matmul(img2,img)
cov=np.cov(img3)
#print(cov)
v,w=np.linalg.eig(cov)
#print("eigen values\n",v,"\neigen vectors\n",w)
e1=w[:1]

pca=np.matmul(e1,np.transpose(img-np.mean(img)))
#print(pca)

print("Image after reduction:",end=" ")
pca=(np.reshape(pca,(r,c)))
print(pca.shape)

plt.subplot(131),plt.imshow(original,cmap='gray'),plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(pca,cmap='gray'),plt.title("Gray image using PCA")
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(gray,cmap='gray'),plt.title("Gray image without PCA")
plt.xticks([]), plt.yticks([])
plt.show()