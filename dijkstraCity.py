import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def menorCaminho(distancia, sptSet, nvertices):
    menor = sys.maxsize
    indiceMenor = False
    for i in range(nvertices):
        if distancia[i] < menor and sptSet[i] == False:
            menor = distancia[i]
            indiceMenor = i

    return indiceMenor

def dijkstra(grafo, source, vertices):
    dist = [sys.maxsize] * vertices
    dist[source] = 0
    sptSet = [False] * vertices
    temp = [[] for m in range(vertices)]

    for cout in range(vertices):
        u = menorCaminho(dist, sptSet, vertices)
        sptSet[u] = True
        
        for v in range(vertices):
            if grafo[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + grafo[u][v]:
                dist[v] = dist[u] + grafo[u][v]

    indice = 0
    for j in dist:
        if j == sys.maxsize:
            print("Sem caminho entre " + str(source) +" e",indice)
        else:
            print("Menor distancia entre " + str(source) +" e",indice,"=",j)
        indice = indice+1


vertices = input()
vertices = int(vertices)
'''

#Grafos para teste


grafo = [
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
            [0,0,0,0]
        ]
grafo = [[0,10,4],
         [0,0,4],
         [2,5,0]]

'''
grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]


dijkstra(grafo, vertices, 9)

#plota o gráfico
A = np.array(grafo)
G = nx.from_numpy_matrix(A,create_using=nx.MultiDiGraph(), parallel_edges=True)
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, connectionstyle='arc3, rad = 0.1',with_labels=True)
plt.show()