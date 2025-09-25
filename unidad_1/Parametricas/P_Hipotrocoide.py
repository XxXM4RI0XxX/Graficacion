import math
import cv2 as cv
import numpy as np
import random as ran

def F1 (R,r,t):
    res = ((R - r)/r)*t
    return res

#Definir dimension de la ventana
img_width,img_height = 800,800

#Crear ventana
img = np.zeros((img_height, img_width, 3), np.uint8)

#Conseguir centro de la imagen
x_i , y_i = img_width // 2, img_height // 2

#Escalar figura a mas grande
escalado = 2
#Declarar el angulo theta inicial
t = 0
#
R = 10
#
r = 30
#
d = 60

while True:

    Rd,Bl,Gr = ran.randint(0,255),ran.randint(0,255),ran.randint(0,255)

    x = int(x_i - escalado * ((R - r)*math.cos(t) +  d*math.cos(F1(R,r,t))))
    y = int(y_i - escalado * ((R - r)*math.sin(t) +  d*math.sin(F1(R,r,t))))

    cv.circle(img, (x, y), 3, (Rd, Bl, Gr), -1)
    t += 0.01
    cv.imshow("image", img)
    cv.waitKey(1)