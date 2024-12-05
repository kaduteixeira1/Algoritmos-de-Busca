import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(grafo):
    G = nx.Graph()

    # Adicionando as arestas ao grafo do NetworkX
    for origem, adjacentes in grafo.adjacencia.items():
        for destino, peso in adjacentes:
            G.add_edge(origem, destino, weight=peso)

    # Desenho do grafo
    pos = nx.spring_layout(G)  # Layout para organizar os nós
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)
    labels = nx.get_edge_attributes(G, 'weight')  # Pega os pesos das arestas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
