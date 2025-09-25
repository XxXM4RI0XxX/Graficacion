import math
import cv2 as cv
import numpy as np

img = cv.imread('Bitwise/img.png',0)
print(img.shape)
x , y = img.shape

new_img_1 = np.zeros((x * 2, y * 2), dtype=np.uint8)
new_img_2 = np.zeros((x * 2, y * 2), dtype=np.uint8)

z,w = 5,2

xx,yy = new_img_1.shape

cx,cy = int(x // 2),int(y // 2)

for i in range(x):
    for j in range(y):
        new_x = int(((i-cy*z) * math.cos(60) + (j-cx*z) * math.sin(60))*0.5)
        new_y = int((-(i-cy*z) * math.sin(60) + (j-cx*z) * math.cos(60))*0.5)
        if 0 <= new_x < yy and 0 <= new_y < xx:
            new_img_1[new_y, new_x] = img[i,j]

xx , yy = new_img_2.shape

for i in range(x):
    for j in range(y):
        new_x = int((((i-cy*w) * math.cos(60) + (j-cx*w) * math.sin(60))*0.8)*2)
        new_y = int(((-(i-cy*w) * math.sin(60) + (j-cx*w) * math.cos(60))*0.8)*2)
        if 0 <= new_x < yy and 0 <= new_y < xx:
            new_img_2[new_y, new_x] = img[i,j]

cv.imshow("img", img)
cv.imshow("IMG 1", new_img_1)
cv.imshow("IMG 2", new_img_2)
cv.waitKey(0)
cv.destroyAllWindows()