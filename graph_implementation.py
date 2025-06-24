class Graph_unidirected:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  # because it's undirected

    def get_graph(self):
        return self.graph 
class Graph_directed: 
    def __init__(self):
        self.graph = {} 
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = [] 
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)  
    def get_graph(self):
        return self.graph 
              
