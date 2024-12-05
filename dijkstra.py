import heapq

def dijkstra(grafo, inicio, destino=None):
    # Inicializa as distâncias e a estrutura de rastreamento
    distancias = [float('inf')] * grafo.vertices
    distancias[inicio] = 0
    anteriores = [None] * grafo.vertices  # Para reconstruir o caminho mais curto
    visitados = set()  # Para rastrear os nós visitados
    fila_prioridade = [(0, inicio)]  # (distância acumulada, vértice)
    caminho_percorrido = []  # Para registrar o caminho completo percorrido

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if vertice_atual in visitados:
            continue

        # Marca o vértice atual como visitado
        visitados.add(vertice_atual)
        caminho_percorrido.append(vertice_atual)

        # Se o destino for encontrado, reconstrói e retorna o caminho
        if vertice_atual == destino:
            caminho_mais_curto = []
            while vertice_atual is not None:
                caminho_mais_curto.append(vertice_atual)
                vertice_atual = anteriores[vertice_atual]
            return list(reversed(caminho_mais_curto))
            

        # Explora os vizinhos do vértice atual
        for vizinho, peso in grafo.adjacencia[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # Retorna apenas o caminho completo se não houver destino específico
    return caminho_percorrido

