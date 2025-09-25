import cv2
import numpy as np

# Crear una imagen en negro
img = np.zeros((300, 300), dtype=np.uint8)

# Dibujar un rectángulo blanco
cv2.rectangle(img, (50, 50), (250, 250), 255, -1)

# Aplicar la operación bitwise NOT
result = cv2.bitwise_not(img)

# Mostrar las imágenes
cv2.imshow("Original", img)
cv2.imshow("NOT Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()