import networkx as nx
import matplotlib.pyplot as plt
import heapq

rutas = {}
with open('rutas.txt', 'r') as file:
    for line in file:
        line = line.replace('"', '')
        salida, destino, costo = line.strip().split(', ')
        costo = int(costo)
        rutas.setdefault(salida, {})[destino] = costo
        rutas.setdefault(destino, {})[salida] = costo

print("Las rutas establecidas son: ")
print(rutas)

G = nx.Graph()

for estacion in rutas.keys():
    G.add_node(estacion)
for salida, destinos in rutas.items():
    for destino, costo in destinos.items():
        G.add_edge(salida, destino, weight=costo)

nx.draw(G, with_labels=True, node_color="purple", node_size=300)
plt.margins(0.2)


def djk(rutas, inicio):
    distancias = {nodo: float('inf') for nodo in rutas}
    rutas_completadas = {nodo: [] for nodo in rutas}
    distancias[inicio] = 0
    priority_Queue = [(0, inicio)]

    while priority_Queue:
        distancia_actual, node_actual = heapq.heappop(priority_Queue)

        for vecino, costo_De_Vecino in rutas[node_actual].items:
            distancia_actualizada = distancia_actual + costo_De_Vecino

            if distancia_actualizada < distancias[vecino]:
                distancias[vecino] = distancia_actualizada
                rutas_completadas[vecino] = rutas_completadas[node_actual] + [node_actual]
                heapq.heappush(priority_Queue, (distancia_actualizada, vecino))

    return distancias, rutas_completadas


def mostrar_rutas_y_costos(rutas, inicio):
    distancias, rutas_completas = djk(rutas, inicio)

    print(f"\nDesde '{inicio}':")
    for destino, costo in distancias.items():
        if destino != inicio:
            ruta = rutas_completas[destino] + [destino]
            if costo < float('inf'):
                print(f"  - Hasta '{destino}': Ruta: {ruta}, Costo: {costo}")
            else:
                print(f"  - Hasta '{destino}': Ruta no encontrada")
