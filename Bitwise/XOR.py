import cv2
import numpy as np

# Crear dos imágenes en negro
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# Dibujar un rectángulo blanco en img1
cv2.rectangle(img1, (50, 50), (250, 250), 255, -1)

# Dibujar un círculo blanco en img2
cv2.circle(img2, (150, 150), 100, 255, -1)

# Aplicar la operación bitwise XOR
result = cv2.bitwise_xor(img1, img2)

# Mostrar las imágenes
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("XOR Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
