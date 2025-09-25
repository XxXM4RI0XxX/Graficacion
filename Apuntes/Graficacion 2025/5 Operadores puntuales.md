Estos operadores son aplicados en cada pixel individual de una imagen, su salida dependerá únicamente de las transformaciones aplicadas a ese pixel específico, ignorando el entorno en el que se encuentra. Es efectivo para **procesamiento de imágenes en tiempo real**, ya que no necesita recopilar información de pixeles vecinos.

> Recordar que una imagen puede ser representada como un modelo continuo $f(x,y)$, donde cada posición $f(x,y)$ representa el valor de un pixel de la matriz $N * M$

# Tipos de operadores

### Identidad
No altera la imagen resultante, el pixel es igual al pixel.
- *Fórmula:* $g(x,y) = f(x,y)$ 

### Negativo
Invierte los pixeles de la imagen, resultando en el negativo de la misma.
- *Fórmula:* $g(x,y) = (L - 1) - f(x,y)$
	Donde $L$ es el valor máximo que puede tener el pixel en la imagen (255 imágenes con un solo canal por ejemplo)

### Umbralización (Thresholding)
Convierte la imagen en una versión binaria. Esto se logra definiendo un umbral (límite) donde los pixeles por encima de ese umbral tendrán un valor (generalmente $255$, blanco) y por debajo de ese umbral tendrán otro (generalmente $0$, negro)
- Fórmula: 
	 ![[Formula Thresholding.png]]

### Corrección Gamma
Ampliamente utilizado en pantallas o fotografías para corregir el brillo o contraste de una imagen.
- *Fórmula:* $g(x,y) = c * f(x,y)^γ$
	- $c$ = constante de escala
	- $γ$ = factor de corrección