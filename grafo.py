class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.adjacencia = {v: [] for v in range(vertices)}

    def adicionar_aresta(self, u, v, peso=1):
        self.adjacencia[u].append((v, peso))
        self.adjacencia[v].append((u, peso))  

    def mostrar_adjacencias(self):
        for vertice, vizinhos in self.adjacencia.items():
            print(f"{vertice} -> {vizinhos}")
    
    def obter_caminho(self, origem, destino, algoritmo):
        if algoritmo == "bfs":
            from bfs import bfs
            caminho_completo = bfs(self, origem)
        elif algoritmo == "dfs":
            from dfs import dfs
            caminho_completo = dfs(self, origem)
        elif algoritmo == "dijkstra":
            from dijkstra import dijkstra
            distancias = dijkstra(self, origem)
            return f"Menor distância de {origem} para {destino}: {distancias[destino]}"
        else:
            raise ValueError("Algoritmo inválido. Escolha 'bfs', 'dfs' ou 'dijkstra'.")
        return caminho_completo


