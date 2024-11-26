def bfs(grafo, inicio, destino=None):
    visitado = [False] * grafo.vertices
    fila = [[inicio]]  
    visitado[inicio] = True

    while fila:
        caminho = fila.pop(0)
        vertice = caminho[-1]

        if vertice == destino:  
            return caminho

        for vizinho, _ in grafo.adjacencia[vertice]:
            if not visitado[vizinho]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                visitado[vizinho] = True

    return None if destino else caminho  
