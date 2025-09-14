import cv2 as cv
import numpy as np

#Window size
w_y = 200
w_x = 300
img = np.ones((w_y, w_x, 3), np.uint8) * 255

#Pos inicial
x = 0
y = 0

mov_derecha = True
mov_abajo = True

for i in range (1000):
    #Redibujar imagen
    img = np.ones((w_y, w_x, 3), np.uint8) * 255

    #Dibujar circulo
    cv.circle(img, (x,y), 20, (255,0,0), -1)

    #Calcular direccion
    if x > w_x:
        mov_derecha = False
    elif x < 0:
        mov_derecha = True
    if y == w_y:
        mov_abajo = False
    elif y < 0:
        mov_abajo = True

    #Mover circulo
    if mov_derecha and mov_abajo:
        x += 1
        y += 1
    elif mov_derecha and not mov_abajo:
        x += 1
        y -= 1
    elif not mov_derecha and mov_abajo:
        x -= 1
        y += 1
    else:
        x -= 1
        y -= 1

    cv.imshow("Rebota pelota",img)
    cv.waitKey(5)

cv.waitKey(0)
cv.destroyAllWindows()