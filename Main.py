import networkx as nx
import matplotlib.pyplot as plt
import heapq

rutas = {}
with open('rutas.txt', 'r') as file:
    for line in file:
        # Limpiar las comillas dobles de la línea
        line = line.replace('"', '')
        salida, destino, costo = line.strip().split(', ')
        costo = int(costo)
        # Agregar rutas con costo
        # Se toma en cuenta para ir de X a Y, y de Y a X
        rutas.setdefault(salida, {})[destino] = costo
        rutas.setdefault(destino, {})[salida] = costo

print("Las rutas establecidas son: ")
print(rutas)

#Generar grafos en base a las rutas
G = nx.Graph()

for estacion in rutas.keys():
    G.add_node(estacion)
for salida, destinos in rutas.items():
    for destino, costo in destinos.items():
        G.add_edge(salida, destino, weight=costo)

nx.draw(G,with_labels=True,node_color="purple",node_size=300)
plt.margins(0.2)

def djk(rutas, inicio):
    distancias = {nodo:float('inf') for nodo in rutas}
    rutas_completadas = {nodo: [] for nodo in rutas}
    distancias[inicio]=0
    priority_Queue = [(0, inicio)]
