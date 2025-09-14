1. Verificar que se tenga la ultima versión de Python
*Se puede ver la version actual de python con:*
```shell
python --version
```
Actualizar obligatoriamente si la versión de python es menor a la 3.10

2.  Instalar OpenCV
```shell
pip install opencv-contrib-python
```

3. Crear un entorno virtual
> Este permitirá la ejecución de OpenCV

```shell
python -m venv nombre_entorno_virtual
```

*Activar el entorno*
```shell
source nombre_entorno_virtual/bin/activate
```

Se puede saber que el entorno esta activado porque se mostrara `(.nombre_entorno_virtual)` al inicio de cada sentencia.

*Desactivar el entorno*
```shell
deactivate
```

*Eliminar el entorno*
```shell
rm -rf nombre_entorno_virtual
```

### Uso e importación en el código

Para utilizar la librería se importa con
```python
import cv2
```

*Leer una imagen*
```python
img = cv2.imread('PATH_imagen')
```

*Convertir una imagen a un espacio de color*
```python
nombre_espacio = cv2.cvtColor(img, cv2.X2Y)
```
Donde:
- $X$ es el espacio de color entrante (la img cargada)
- $Y$ es el espacio de color de salida (la imagen a mostrar)

Por defecto OpenCV lee todas las imágenes en $BGR$,  que es exactamente lo mismo que $RGB$ pero con orden invertido.

Espacios de color comunes en OpenCV:
- $BGR$: RGB pero invertido
- $RGB$: El de toda la vida
- $HSV$: El mas parecido a la vista humana
- $GRAY$: Escala de grises

*Crear una mascara que muestre pixeles dentro de un rango de color en la imagen*
- Primero se define el rango de colores que se van a detectar
```python
rango_alto = np.array([v1,v2,v3])
rango_bajo = np.array([v1,v2,v3])
```
En caso de espacio de color `GRAY`, seria solo 1 valor en ves de un array de valores

- Se crea una máscara que solo incluya los pixeles que cumplan los rangos definidos
```python
mask = cv2.inRange(nompre_espacio, rango_bajo, rango_alto)
```

- Aplicar la máscara a la imagen
```python
resultado = cv2.bitwise_and(img, img, mask=mask)
```

*Mostrar imágenes en ventanas*
```python
cv2.imshow("Titulo ventana", img)
```

*Declarar tiempo de espera antes de abrir ventanas*
```python
cv2.waitKey(0)
```

*Cerrar todas las ventanas*
```python
cv2.destroyAllWindows()
```
