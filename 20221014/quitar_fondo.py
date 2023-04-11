import cv2
import numpy as np

# Cargar imagen
image = cv2.imread("image.jpeg")

# Convertir imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral adaptativo
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Aplicar dilatación y erosión para eliminar ruido
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dilate = cv2.dilate(thresh, kernel, iterations=2)
erode = cv2.erode(dilate, kernel, iterations=2)

# Encontrar contornos y dibujarlos en una imagen en blanco
contours, hierarchy = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask = cv2.drawContours(np.zeros_like(image), contours, -1, (255, 255, 255), -1)

# Aplicar la máscara para eliminar el fondo
result = cv2.bitwise_and(image, mask)

# Guardar imagen resultante
cv2.imwrite("result.jpg", result)