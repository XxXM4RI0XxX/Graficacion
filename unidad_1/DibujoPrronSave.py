import cv2 as cv
import numpy as np

#Crear imagen * escala de gris
color_fondo = 100
img = np.ones((500,500,3), np.uint8) * color_fondo

#Poligono del carro
cuerpo = np.array([[30, 240], [40, 300],  #Defensa trasera
                   [100,320], [450,320],  #Parte baja
                   [460,245],  #Defensa delantera
                   [420,230], [300,215],  #Cofre
                   [255,180], [220,160], [100,170]]) #Techo
cuerpo = cuerpo.reshape((-1, 1, 2))
#Rellenar el poligono
cv.fillPoly(img, [cuerpo], (220, 50, 10))
#Faro
cv.rectangle(img, (420,230), (470,260), (0,220,220),-1)
cv.line(img, (420,230),(420,260),(0,0,0),2)
cv.line(img, (470,260),(420,260),(0,0,0),2)
#Contorno del poligono: polylines(img, [arreglo_pts], cerrar_primer_ultimo_pto, (r,g,b), grosor)
cv.polylines(img, [cuerpo], True, (0, 0, 0), 2)

#Ventanas
ventana = np.array([[290,215],[250, 185], [220, 167], [105, 177], [65, 215]])
cv.polylines(img, [ventana], True, (0, 0, 0), 3)
cv.fillPoly(img,[ventana], (255,255,0))

#Puertas
#puerta = np.array([[65,215],[],[290,215]])

#Rueda 1
cc1 = 120
cv.circle(img, (cc1, 310), 45, (0, 0, 0), -1) #LLanta
cv.circle(img, (cc1, 310), 25, (100, 100, 100), -1) #Rin exterior
cv.circle(img, (cc1, 310), 10, (150, 150, 150), -1) #Rin interior

#Rueda 2
cc2 = 375
cv.circle(img, (cc2, 310), 45, (0, 0, 0), -1) #LLanta
cv.circle(img, (cc2, 310), 25, (100, 100, 100), -1) #Rin exterior
cv.circle(img, (cc2, 310), 10, (150, 150, 150), -1) #Rin interior

#Cubrir foco
cv.line(img, (460,320), (470,245), (color_fondo, color_fondo, color_fondo), 15)
cv.line(img, (460,235), (420,220), (color_fondo, color_fondo, color_fondo), 15)
cv.circle(img, (465,230), 15, (color_fondo, color_fondo, color_fondo), -1)

cv.imshow("Carro shido xd",img)
cv.waitKey(0)
cv.destroyAllWindows()