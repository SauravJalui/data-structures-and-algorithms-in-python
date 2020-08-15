import numpy as np
from queue_linkedlist import LinkedQueue
class Graph:
    def __init__(self, vertices):
        self.adjmat = np.zeros((vertices, vertices))
        self.vertices = vertices
        self.visited = [0] * self.vertices

    def insert_edge(self, u, v, w = 1):
        self.adjmat[u][v] = w

    def delete_edge(self, u, v):
        self.adjmat[u][v] = 0

    def get_edge(self, u, v):
        return self.adjmat[u][v]

    def vertices_count(self):
        return self.vertices

    def edge_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if not self.adjmat [i][j] == 0:
                    count += 1
        return count

    def indegree(self, u):
        count = 0
        for i in range(self.vertices):
            if not self.adjmat[i][u] == 0:
                count += 1
        return count

    def outdegree(self, u):
        count = 0
        for i in range(self.vertices):
            if not self.adjmat[u][i] == 0:
                count += 1
        return count

    def display(self):
        print(self.adjmat)

    def DFS(self, i):
        if self.visited[i] == 0:
            print (i, end="==>")
            self.visited[i] = 1
            for j in range(self.vertices):
                if self.adjmat[i][j] == 1 and self.visited[j] == 0:
                    self.DFS(j)

G = Graph(7)
G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
G.DFS(0)