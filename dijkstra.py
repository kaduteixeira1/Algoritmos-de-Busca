import heapq

def dijkstra(grafo, inicio, destino=None):
    distancias = [float('inf')] * grafo.vertices
    distancias[inicio] = 0
    anteriores = [None] * grafo.vertices
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if vertice_atual == destino:  
            caminho = []
            while vertice_atual is not None:
                caminho.append(vertice_atual)
                vertice_atual = anteriores[vertice_atual]
            return list(reversed(caminho))

        for vizinho, peso in grafo.adjacencia[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return distancias if destino is None else None  
