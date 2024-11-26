class GrafoK:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append((peso, u, v))

    def encontrar(self, pai, vertice):
        if pai[vertice] == vertice:
            return vertice
        return self.encontrar(pai, pai[vertice])

    def unir(self, pai, rank, u, v):
        raiz_u = self.encontrar(pai, u)
        raiz_v = self.encontrar(pai, v)

        if rank[raiz_u] < rank[raiz_v]:
            pai[raiz_u] = raiz_v
        elif rank[raiz_u] > rank[raiz_v]:
            pai[raiz_v] = raiz_u
        else:
            pai[raiz_v] = raiz_u
            rank[raiz_u] += 1

    def kruskal(self):
        # Ordenar as arestas por peso
        self.arestas.sort()
        pai = []
        rank = []
        mst = []
        peso_total = 0

        # Inicializar estruturas
        for vertice in range(self.vertices):
            pai.append(vertice)
            rank.append(0)

        # Iterar pelas arestas ordenadas
        for aresta in self.arestas:
            peso, u, v = aresta
            if self.encontrar(pai, u) != self.encontrar(pai, v):
                mst.append(aresta)
                peso_total += peso
                self.unir(pai, rank, u, v)

        return mst, peso_total

    def mostrar_mst(self):
        mst, peso_total = self.kruskal()
        print("Árvore Geradora Mínima (MST):")
        for peso, u, v in mst:
            print(f"Aresta {u}-{v}, Peso: {peso}")
        print(f"Peso Total da MST: {peso_total}")


grafo = GrafoK(6)
grafo.adicionar_aresta(0, 1, 4)
grafo.adicionar_aresta(0, 2, 4)
grafo.adicionar_aresta(1, 2, 2)
grafo.adicionar_aresta(1, 3, 5)
grafo.adicionar_aresta(2, 3, 8)
grafo.adicionar_aresta(3, 4, 6)
grafo.adicionar_aresta(4, 5, 9)
grafo.adicionar_aresta(3, 5, 7)

grafo.mostrar_mst()
