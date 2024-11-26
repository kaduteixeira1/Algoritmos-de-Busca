def dfs(grafo, inicio, destino=None, visitado=None, caminho=None):
    if visitado is None:
        visitado = [False] * grafo.vertices
    if caminho is None:
        caminho = []

    visitado[inicio] = True
    caminho.append(inicio)

    if inicio == destino:  
        return caminho

    for vizinho, _ in grafo.adjacencia[inicio]:
        if not visitado[vizinho]:
            resultado = dfs(grafo, vizinho, destino, visitado, caminho)
            if resultado:
                return resultado

    caminho.pop()
    return None if destino else caminho
