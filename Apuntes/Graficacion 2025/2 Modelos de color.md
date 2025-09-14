### Modelos de color
Son representaciones matemáticas que describen como los colores pueden ser representados de diversas formas utilizando valores numéricos
##### RGB (Red, Green, Blue)
En el modelo RGB, los colores se generan mediante la combinación de luz. Cuanto más intensa es la luz en cada canal (rojo, verde o azul), más claro es el color resultante. Cuando todas las intensidades están al máximo, el color resultante es blanco; cuando todas las intensidades están al mínimo, el resultado es negro.
###### Aplicaciones de RGB
- Monitores y pantallas
- Cámaras digitales
- Gráficos por computadora

#### CMY (Cyan, Magenta, Yellow)
Es un modelo me mezcla substractiva. Cada color se describe en base a cuanto absorbe cada tinta la luz blanca que incide en el papel de impresión (normalmente blanco).
Cada tinta absorbe ciertos colores y refleja el resto:
- **Cian (C):** absorbe Rojo y refleja Verde + Azul.
- **Magenta (M):** absorbe Verde y refleja Rojo + Azul.
- **Amarillo (Y):** absorbe Azul y refleja Rojo + Verde.

### CMYK (Cyan, Magenta, Yellow, Black)
Sigue los mismos principios que el CMY, con la diferencia que adiciona el uso de *tinta negra*. Esto es porque al combinar $C + M + Y$ da un tono gris muy oscuro, lo cual afecta a la hora de impresiones en blanco y negro por ejemplo. Adicionar la *tinta negra* soluciona este problema.

Este es lo modelo más utilizado en tareas de **impresión**.

### HSV (Hue, Saturation, Value)
Este modelo representa los colores de una manera mas cercana a como los humanos vemos los colores.
- $H$ *(Hue)*:  Hue, o tono, es el color puro, medio en grados
	- 0º = Rojo
	- 120º = Verde
	- 240º = Azul
	- 360º = Regresa a rojo
- $S$ *(Saturation)*: Cuán intenso es ese color
	- 0% Desaturado (gris)
	- 100% Vivo y puro
- $V$ *(Value)*: Cantidad de luz del color
	- 0% Negro total
	- 100% El color más claro posible en ese tono

### HSL (Hue, Saturation, Lightness)
Es similar a $HSV$, solo que utiliza luminosidad envés de un valor. La luminosidad representa la cantidad de luz que refleja un color.
Entonces:
- $H$ *(Hue)*: Mismo que en HSV
- $S$ *(Saturation)*: Parecido a HSV
- $L$ *(Luminosidad)*: Cuanta luz es reflejada. Valores de 0 a 1.
	- $0$ = Negro
	- $0.5$ = Color puro
	- $1$ = Blanco
Es muy utilizado en herramientas de diseño gráfico. donde se necesita tener un control preciso sobre la luz y color.