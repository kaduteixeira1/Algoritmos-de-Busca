from grafo import Grafo
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra
from desenhar_grafo import desenhar_grafo

def main():
    grafo = Grafo(12) 

    grafo.adicionar_aresta(0, 1, 1)
    grafo.adicionar_aresta(0, 2, 4)
    grafo.adicionar_aresta(1, 3, 3)
    grafo.adicionar_aresta(2, 4, 2)
    grafo.adicionar_aresta(3, 5, 1)
    grafo.adicionar_aresta(4, 5, 5)
    grafo.adicionar_aresta(5, 6, 2)
    grafo.adicionar_aresta(6, 7, 3)
    grafo.adicionar_aresta(7, 8, 1)
    grafo.adicionar_aresta(8, 9, 4)
    grafo.adicionar_aresta(9, 10, 2)
    grafo.adicionar_aresta(10, 11, 3)
    grafo.adicionar_aresta(11, 0, 5) 
    
    print("Lista de adjacências:")
    grafo.mostrar_adjacencias()

    # Testar BFS
    print("\nCaminhamento em largura (BFS) a partir do vértice 0:")
    print("Caminho completo:", bfs(grafo, 0))
    print("Caminho até o vértice 11:", bfs(grafo, 0, destino=11))

    # Testar DFS
    print("\nCaminhamento em profundidade (DFS) a partir do vértice 0:")
    print("Caminho completo:", dfs(grafo, 0))
    print("Caminho até o vértice 11:", dfs(grafo, 0, destino=11))

    # Testar Dijkstra
    print("\nMenores distâncias (Dijkstra) a partir do vértice 0:")
    print("Todas as distâncias:", dijkstra(grafo, 0))
    print("Caminho mais curto até o vértice 11:", dijkstra(grafo, 0, destino=11))

    # Desenhar o grafo
    desenhar_grafo(grafo)

if __name__ == "__main__":
    main()
