from grafo import Grafo
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

def main():
    grafo = Grafo(6)
    grafo.adicionar_aresta(0, 1, 1)
    grafo.adicionar_aresta(0, 2, 4)
    grafo.adicionar_aresta(1, 3, 3)
    grafo.adicionar_aresta(2, 4, 2)
    grafo.adicionar_aresta(3, 5, 1)
    grafo.adicionar_aresta(4, 5, 5)

    print("Lista de adjacências:")
    grafo.mostrar_adjacencias()

    # Testar BFS
    print("\nCaminhamento em largura (BFS) a partir do vértice 0:")
    print("Caminho completo:", bfs(grafo, 0))
    print("Caminho até o vértice 5:", bfs(grafo, 0, destino=5))

    # Testar DFS
    print("\nCaminhamento em profundidade (DFS) a partir do vértice 0:")
    print("Caminho completo:", dfs(grafo, 0))
    print("Caminho até o vértice 5:", dfs(grafo, 0, destino=5))

    # Testar Dijkstra
    print("\nMenores distâncias (Dijkstra) a partir do vértice 0:")
    print("Todas as distâncias:", dijkstra(grafo, 0))
    print("Caminho mais curto até o vértice 5:", dijkstra(grafo, 0, destino=5))

if __name__ == "__main__":
    main()
