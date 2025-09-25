import cv2 as cv
import numpy as np
import math

from unidad_1.ejemplo_tras_rot_esc import new_x

img = cv.imread('Bitwise/img.png',0)

#Alto,ancho de la imagen original
x,y = img.shape

#Crear una nueva imagen en blanco, del doble del tamaño de la orginial (x,y * 2)
rotated_img = np.zeros((x*2,y*2), dtype=np.uint8)

#Alto, ancho de la imagen en blanco
xx,yy = rotated_img.shape

#Centro de la imagen original
cx,cy = int(x//2),int(y//2)

#Angulo de rotacion
angle = 45
theta = math.radians(angle)

for i in range(x):
    for j in range(y):
        new_x = j+cx
        new_y = i+cy
        if 0 <= new_x < yy and 0 <= new_y < xx:
            rotated_img[new_y,new_x] = img[i,j]

cv.imshow('img',img)
cv.imshow('rotated_img',rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()