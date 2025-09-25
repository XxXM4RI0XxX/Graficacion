import cv2 as cv
import numpy as np
import math

img = cv.imread("Bitwise/paisaje.jpeg",0)

print(img.shape)
x, y = img.shape

rotaded_img = np.zeros((x*2,y*2), dtype=np.uint8)

xx,yy = rotaded_img.shape

cx,cy = int(x // 2),int(y // 2)

angle = 45
theta = math.radians(angle)

for i in range(x):
    for j in range(y):
#        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
#       new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        new_x = int(((i * math.cos(theta) + j * math.sin(theta))+100)*0.5)
        new_y = int(((-i * math.sin(theta) + j * math.cos(theta))+100)*0.5)
        if 0 <= new_x < yy and 0 <= new_y < xx:
            rotaded_img[new_y, new_x] = img[i,j]

cv.imshow("", rotaded_img)
cv.waitKey(0)
cv.destroyAllWindows()