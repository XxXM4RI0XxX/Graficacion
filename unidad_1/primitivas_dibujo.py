import cv2
import numpy as np

#Crear imagen de 500 x 500 en un solo canal
 #img = np.ones((500,500), np.uint8)*150
#Crear imagen de 500 x 500 en 3 canales (de color)
img = np.ones((500,500,3), np.uint8)*150
#Crear circulo (imagen_donde_se_crea, (posicion_central_x_y), radio, (color_rgb), relleno? -1 = si, nada = no)
cv2.circle(img,(255,255),100,(23,43,144),-1)
#Circulo radio = 1 -> Punto en el plano
#Crear rectangulo (img, P1(x,y), P2(x,y), (color), relleno?)
cv2.rectangle(img,(10,10),(200,100),(34,56,100),-1)
#Crear linea (img, P1(x,y), P2(x,y), (r,g,b), grosor)
cv2.line(img, (255,255), (200,100), (23,244,144), 4)
#Polylines, hacer linea uniendo puntos, usando un arreglo de puntos
#cv2.polylines(img,)

for i in range(400):
    cv2.circle(img, (i,i), 3, (255,0,0), -1)
    cv2.imshow("img", img)
    cv2.waitKey(20)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()