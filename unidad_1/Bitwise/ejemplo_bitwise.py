import cv2
import numpy as np

# Cargar la imagen principal
img1 = cv2.imread('paisaje.jpeg')

# Cargar la imagen que queremos enmascarar
img2 = cv2.imread('img.png')

# Obtener las dimensiones de la segunda imagen (logo)
rows, cols, channels = img2.shape

# Definir la región de interés (ROI) en la imagen principal
roi = img1[0:rows, 0:cols]

# Convertir la imagen del logo a escala de grises
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Crear una máscara binaria a partir de la imagen en escala de grises
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

# Invertir la máscara
mask_inv = cv2.bitwise_not(mask)

# Hacer visible el fondo de la imagen principal en la región del logo
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Extraer el logo
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Combinar el fondo y el logo
dst = cv2.add(img1_bg, img2_fg)

# Colocar la imagen combinada en la imagen principal
img1[0:rows, 0:cols] = dst

# Mostrar la imagen final
cv2.imshow("Resultado", img1)
cv2.waitKey(0)