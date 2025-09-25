import math

import cv2 as cv
import numpy as np

#Definir dimension de la ventana
img_width,img_height = 800,800

#Crear ventana
img = np.zeros((img_height, img_width, 3), np.uint8)

#Conseguir centro de la imagen
x_i , y_i = img_width // 2, img_height // 2

#Declarar el angulo theta
theta = 0

while True:

    # Ecuacion de la parametrica
    # Se hace el casteo a dato entero porque cv.circle solo acepta enteros
    # para la coordenada central
    # Al ser una parametrica, el unico valor que cambia es el angulo theta
    # por lo que, el punto central nunca cambia, y solo se le suma el resultado
    # de la ecuacion
    # Cada iteracion del ciclo, el valor del angulo se cambia, y nuevo punto
    # en la ecuacion parametrica es graficado
    # La multiplicacion 100 * Ec..., sirve para escalar la animacion
    x = int(x_i + 100*(math.cos(3 * theta) - math.cos(2 * theta)**5))
    y = int(y_i + 100*(math.sin(4 * theta) - math.sin(3 * theta)**2))

    cv.circle(img, (x, y), 2, (255, 255, 255), -1)
    theta += 0.01
    cv.imshow("image", img)
    cv.waitKey(10)
cv.waitKey(0)
cv.destroyAllWindows()