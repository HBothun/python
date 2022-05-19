import cv2
import numpy as np
import random


def encrypt(in1, in2, out):
    img1 = cv2.imread(in1)
    img2 = cv2.imread(in2)
      
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for l in range(3):
                v1 = format(img1[i][j][l], '08b')
                v2 = format(img2[i][j][l], '08b')
                v3 = v1[:4] + v2[:4]                   
                img1[i][j][l]= int(v3, 2)                  
    cv2.imwrite(out, img1)
  
def decrypt(input, out1, out2):
    img = cv2.imread(input) 
    width = img.shape[0]
    height = img.shape[1]
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)      
    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '08b')
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                img1[i][j][l]= int(v2, 2)
                img2[i][j][l]= int(v3, 2)
    cv2.imwrite(out1, img1)
    cv2.imwrite(out2, img2)

encrypt('Cv2\Steganography\pic1.jpg', 'Cv2\Steganography\Test.png', 'Cv2\Steganography\TextBlend.png')
decrypt('Cv2\Steganography\TextBlend.png', 'Cv2\Steganography\pic1de.png','Cv2\Steganography\Testde.png')