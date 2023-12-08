# Daniel Pinto 15-11139, Pedro Rodriguez 15-11264

## Parte 1: Detalles de la implementacion.

El algoritmo de KMeans no especifica como lidiar en las siguientes situaciones:

- Un centroide no tiene ningún elemento asignado.
- Los centroides iniciales están repetidos.
- Los centroides parecen no converger.

Por lo que en nuestra implementaición del algoritmo decidimos:

- Conservar estos centroides a pesar de que estén vacíos, por lo que nuestro algoritmo genera a los sumo $k$ centroides.
- Mantener estos centroides, sin embargo, esta decisión surge más por una incapacidad de no poder asegurar $k$ centroides iniciales aleatorios con distintos valores, por lo que queda como ejercicio para un próximo experimento con este algoritmo.
- Colocamos un máximo de iteraciones en caso de que los centroides no convergan en una cantidad de tiempo aceptable.

## Parte 2: Iris Dataset

A continuación se presentan los resultados de aplicar KMeans al Iris Dataset, donde:

- El eje x es "sepal_lenght".
- El eje y es "sepal_width".
- El eje z es "petal_length".
- La escala de los puntos es "petal_width".
- Los colores representan distintos clusters.

<p align="center">
  <img src="./imgs/iris_k2_its300.jpg" alt="KMeans de iris.csv con k = 2"/>
   <figcaption style="text-align: center;">KMeans de iris.csv con k = 2</figcaption>
</p>

<p align="center">
  <img src="./imgs/iris_k3_its300.jpg" alt="KMeans de iris.csv con k = 3"/>
   <figcaption style="text-align: center;">KMeans de iris.csv con k = 3</figcaption>
</p>

<p align="center">
  <img src="./imgs/iris_k4_its300.jpg" alt="KMeans de iris.csv con k = 4"/>
   <figcaption style="text-align: center;">KMeans de iris.csv con k = 4</figcaption>
</p>

<p align="center">
  <img src="./imgs/iris_k5_its300.jpg" alt="KMeans de iris.csv con k = 5"/>
   <figcaption style="text-align: center;">KMeans de iris.csv con k = 5</figcaption>
</p>

## Parte 3: Segmentación de Imagenes

Las imagenes escogidas para esta parte son las siguientes:

<p align="center">
  <img src="./imgs/1.jpg" alt="4 círculos de color"/>
   <figcaption style="text-align: center;">4 círculos de color</figcaption>
</p>

<p align="center">
  <img src="./imgs/2.jpg" alt="Loro colorido"/>
   <figcaption style="text-align: center;">Loro colorido</figcaption>
</p>

Siendo la primera escogida por su simplicidad y estar compuesta por únicamente 5 colores planos (blanco, verde, azul, morado y amarillo), y la segunda debido a su complejidad y variedad de colores. Los experimentos se realizaron para $k=2$ $k=3$ $k=4$ $k=5$ $k=10$ $k=20$ y $k=40$, cada uno con un máximo de $300$ iteraciones.

## Imágenes resultantes

### Imagen 1
<p align="center">
  <img src="./imgs/im1_k2_its300.jpg" alt="Imágen 1 k=2"/>
   <figcaption style="text-align: center;">Imágen 1 k=2</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k3_its300.jpg" alt="Imágen 1 k=3"/>
   <figcaption style="text-align: center;">Imágen 1 k=3</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k4_its300.jpg" alt="Imágen 1 k=4"/>
   <figcaption style="text-align: center;">Imágen 1 k=4</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k5_its300.jpg" alt="Imágen 1 k=5"/>
   <figcaption style="text-align: center;">Imágen 1 k=5</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k10_its300.jpg" alt="Imágen 1 k=10"/>
   <figcaption style="text-align: center;">Imágen 1 k=10</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k20_its300.jpg" alt="Imágen 1 k=20"/>
   <figcaption style="text-align: center;">Imágen 1 k=20</figcaption>
</p>

<p align="center">
  <img src="./imgs/im1_k40_its300.jpg" alt="Imágen 1 k=40"/>
   <figcaption style="text-align: center;">Imágen 1 k=40</figcaption>
</p>

### Imagen 2

<p align="center">
  <img src="./imgs/im2_k2_its300.jpg" alt="Imágen 2 k=2"/>
   <figcaption style="text-align: center;">Imágen 2 k=2</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k3_its300.jpg" alt="Imágen 2 k=3"/>
   <figcaption style="text-align: center;">Imágen 2 k=3</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k4_its300.jpg" alt="Imágen 2 k=4"/>
   <figcaption style="text-align: center;">Imágen 2 k=4</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k5_its300.jpg" alt="Imágen 2 k=5"/>
   <figcaption style="text-align: center;">Imágen 2 k=5</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k10_its300.jpg" alt="Imágen 2 k=10"/>
   <figcaption style="text-align: center;">Imágen 2 k=10</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k20_its300.jpg" alt="Imágen 2 k=20"/>
   <figcaption style="text-align: center;">Imágen 2 k=20</figcaption>
</p>

<p align="center">
  <img src="./imgs/im2_k40_its300.jpg" alt="Imágen 2 k=40"/>
   <figcaption style="text-align: center;">Imágen 2 k=40</figcaption>
</p>

### Observaciones

En general, podemos observar que mientras tengamos una mayor cantidad $k$ de clusters, la imagen generada tra aplicar KMeans va a tener mayor detalle y profundidad de colores, sin embargo destaca la paleta de colores obtenidas para ambas imágenes. Para la imagen 1, la paleta de colores obtenida parece corresponder a aquellos tonos que pueden encontrarse de manera significativa en esta, y unicamente para $k<=5$ obtenemos coloraciones que no corresponden a la imagen, probablemente debido a que no se crean suficientes clusters para agrupar los distintos colores de la imagen en sus propios grupos, teniendo que generarse así un color calculado con la media. 

Adicionalmente, los bordes de las figuras parecen siempre variar entre más de un cluster, generando una especie de ruido delimitador (curiosamente como una especie de edge detection) en la frontera entre 2 colores que parece ser consecuencia de que los píxeles en el contorno de los círculos probablemente tengan un degradado imperceptible para el ojo humano. 

Los resultados de la imagen 2 tienen un comportamiento similar a la primera pero con un efecto mucho más notorio debido a la extrema variedad y complejidad de los colores disponibles en esta. Al haber una gran variedad de colores en la imagen, no se crea una cantidad de clusters suficientemente representativa para todas las coloraciones, por lo que los centroides obtenidos tienen un coloración marrón. Una analogía que parece adecuada para los colores obtenidos, es que si tomamos pinturas/plastilinas de distintos colores y las mezclamos, vamos a obtener un color grisaceo/marrón.