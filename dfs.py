def dfs(grafo, inicio, destino=None):
    visitado = [False] * grafo.vertices
    percurso_completo = []  
    menor_caminho = []     

    def explorar(vertice, caminho_atual):
        nonlocal menor_caminho
        visitado[vertice] = True
        percurso_completo.append(vertice)  
        caminho_atual.append(vertice)      

        if vertice == destino:
            menor_caminho = caminho_atual[:]

        for vizinho, _ in grafo.adjacencia[vertice]:
            if not visitado[vizinho]:
                explorar(vizinho, caminho_atual)

        caminho_atual.pop()  # Remove o vértice ao retroceder na pilha

    explorar(inicio, [])

    return percurso_completo, (menor_caminho if destino is not None else None)
