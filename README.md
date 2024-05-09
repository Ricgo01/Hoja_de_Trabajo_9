# Algoritmo de Dijkstra para encontrar la ruta más corta en un sistema de rutas

Este código implementa el algoritmo de Dijkstra en Python para encontrar la ruta más corta entre diferentes lugares en un sistema de rutas. El algoritmo de Dijkstra es una técnica clásica en la teoría de grafos que encuentra la ruta más corta desde un nodo inicial a todos los demás nodos en un grafo ponderado.

# Cómo funciona:

1. **Carga de datos:** El código lee un archivo de texto llamado 'rutas.txt', que describe las conexiones entre lugares y sus costos asociados. Cada línea del archivo representa una ruta con el formato "salida, destino, costo".

2. **Visualización del gráfico de rutas:** Utiliza la biblioteca NetworkX para visualizar las rutas como un grafo, donde cada lugar es un nodo y las rutas son las aristas entre ellos.

3. **Algoritmo de Dijkstra:** La función `djk` implementa el algoritmo de Dijkstra para encontrar la ruta más corta desde un nodo inicial a todos los demás nodos en el grafo. Utiliza una cola de prioridad para seleccionar el próximo nodo a explorar de manera eficiente.

4. **Funciones auxiliares:** El código también incluye funciones para mostrar todas las rutas disponibles, mostrar rutas y costos desde un lugar específico, y un menú interactivo para que el usuario pueda explorar el sistema de rutas.

# Instrucciones de uso:

- Ejecuta el archivo `ruta_corta.py`.
- Selecciona una opción del menú para mostrar rutas establecidas, visualizar el gráfico de rutas o encontrar la ruta más corta desde un lugar específico.

# Estructura del proyecto:

- `ruta_corta.py`: Contiene el código Python que implementa el algoritmo de Dijkstra y proporciona la funcionalidad interactiva.
- `rutas.txt`: Archivo de texto que describe las rutas disponibles en el sistema.
- `README.md`: Este archivo, que proporciona instrucciones de uso y descripción del proyecto.

**Contribuciones:**
Vianka Vanessa Castro Ordoñez - 23201
Ricardo Arturo Godinez Sanchez - 23247

