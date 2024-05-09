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


def mostrar_grafico(rutas):
    G = nx.Graph()
    for estacion in rutas.keys():
        G.add_node(estacion)
    for salida, destinos in rutas.items():
        for destino, costo in destinos.items():
            G.add_edge(salida, destino, weight=costo)

    nx.draw(G, with_labels=True, node_color="purple", node_size=300)
    plt.margins(0.2)
    plt.show()


def djk(rutas, inicio):
    distancias = {nodo: float('inf') for nodo in rutas}
    rutas_completadas = {nodo: [] for nodo in rutas}
    distancias[inicio] = 0
    priority_Queue = [(0, inicio)]

    while priority_Queue:
        distancia_actual, node_actual = heapq.heappop(priority_Queue)

        for vecino, costo_De_Vecino in rutas[node_actual].items():
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
                print(f"  - Hasta {destino}: Ruta: {ruta}, Costo: {costo}")
            else:
                print(f"  - Hasta {destino}: Ruta no encontrada")

def mostrar_rutas(rutas):
    print("Las rutas establecidas son:")
    print("------------------------")
    for salida, destinos in rutas.items():
        print(f"Desde {salida}:")
        for destino, costo in destinos.items():
            print(f"  - {destino}: Costo: {costo}")
    print("------------------------")

def menu():
    while True:
        print("------------------------")
        print("  *** AGENDA DE VIAJES ***")
        print("Bienvenido al Menu de Rutas!!")
        print("1. Mostrar rutas establecidas")
        print("2. Mostrar grafico")

        print("-------Opcion de Rutas-------")

        print("3. Pueblo Paleta")
        print("4. Aldea Azalea")
        print("5. Ciudad Safiro")
        print("6. Aldea Fuego")
        print("7. Ciudad Lavanda")
        print("8. Salir")

        opcion = input("Seleccione una opcion: \n >")

        if opcion == '1':
            mostrar_rutas(rutas)
        elif opcion == '2':
            mostrar_grafico(rutas)
        elif opcion == '3':
            mostrar_rutas_y_costos(rutas, 'Pueblo Paleta')
        elif opcion == '4':
            mostrar_rutas_y_costos(rutas,'Aldea Azalea')
        elif opcion == '5':
            mostrar_rutas_y_costos(rutas,'Ciudad Safiro')
        elif opcion == '6':
            mostrar_rutas_y_costos(rutas, 'Aldea Fuego')
        elif opcion == '7':
            mostrar_rutas_y_costos(rutas, 'Ciudad Lavanda')
        elif opcion == '8':
            print("Gracias por utilizar nuestra agenda de viajes ")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


menu()