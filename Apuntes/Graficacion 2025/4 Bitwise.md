> En OpenCV

La operación *Bitwise* permite comparar los pixeles de dos imágenes (la comparación es 1:1, pixel en la posición $NM$ de la imagen 1, con el pixel en la misma posición $NM$ de la imagen 2) para resultar en una tercer imagen que representa la relación entre los pixeles de las dos imágenes.

### AND
El pixel resultante es $1$, cuando ese pixel en ambas imágenes valga $1$
![[EJ_AND.png]]

### OR
El pixel resultante es $1$, ya sea si ese pixel vale $1$ en una u otra imagen
![[EJ_OR.png]]

### XOR
El pixel resultante será $1$, cuando ese pixel sea $1$ en una y solo una de las dos imágenes
![[EJ_XOR.png]]
(Todos los pixeles de la `img2` coinciden con los de la `img1`, por lo que esos pixeles en ambas imágenes son $1$, haciendo que valgan $0$ en el resultado. Los pixeles restantes en la `img1` solo son $1$ en esa imagen, por que en el resultado valen $1$)

### NOT
Simple, solo se aplica a una imagen. Toma los pixeles de esa imagen e invierte su valor
![[EJ_NOT.png]]
