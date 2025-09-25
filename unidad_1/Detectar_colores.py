import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('../source/Hollow Knight Plushes (smoll).png')

# Convertir la imagen al espacio de color HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir el rango inferior y superior para detectar verde
lower_green = np.array([40, 50, 100])  # Hue, Saturación, Brillo mínimos
upper_green = np.array([80, 200, 255])  # Hue, Saturación, Brillo máximos

# Crear una máscara que solo incluya los píxeles dentro del rango
mask = cv2.inRange(hsv, lower_green, upper_green)

# Aplicar la máscara a la imagen original
result = cv2.bitwise_not(img, img, mask=mask)

# Mostrar la imagen original y la imagen con el color detectado
cv2.imshow("Imagen Original", img)
cv2.imshow("Color Detectado", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#trasladar
#rotar
#Sizallar
#escalar