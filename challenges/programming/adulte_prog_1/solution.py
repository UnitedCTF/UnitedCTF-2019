
class RateGraph(object):
    def __init__(self, rates):
        'Initialize the graph from an iterable of (start, end, rate) tuples.'
        self.graph = {}
        for orig, dest, rate in rates:
            self.add_conversion(orig, dest, float(rate))

    def add_conversion(self, orig, dest, rate):
        'Insert a conversion into the graph. Note we insert its inverse also.'
        if orig not in self.graph:
            self.graph[orig] = {}
        self.graph[orig][dest] = rate

        if dest not in self.graph:
            self.graph[dest] = {}
        self.graph[dest][orig] = 1.0 / rate


    def get_neighbors(self, node):
        'Returns an iterable of the nodes neighboring the given node.'
        if node not in self.graph:
            return None
        return self.graph[node].items()


    def get_nodes(self):
        'Returns an iterable of all the nodes in the graph.'
        return self.graph.keys()

    def bfs(self, start, end):
        to_visit = deque()
        to_visit.appendleft((start, 1.0))
        visited = set()

        while to_visit:
            node, rate_from_origin = to_visit.pop()
            if node == end:
                return rate_from_origin
            visited.add(node)
            for unit, rate in self.get_neighbors(node):
                if unit not in visited:
                    to_visit.appendleft((unit, rate_from_origin * rate))

        return None

from collections import deque


conversions = []
with open("conversions.txt", "r") as file:
    lignes = file.readlines()
    for ligne in lignes:
        ahah = ligne.strip().split()
        conversions.append(tuple(ahah))

graph = RateGraph(conversions)

aConvertir = []
with open("aConvertir.txt", "r") as file:
    lignes = file.readlines()
    for ligne in lignes:
        ahah = ligne.strip().split()
        aConvertir.append(tuple([float(ahah[0]), ahah[1], ahah[2]]))

resultatFinal = 0
for initial, source, destination in aConvertir:
    resultat = graph.bfs(source, destination)
    if resultat is None:
        yes = 0
        print(f"{source} {destination} None")
    else:
        yes = initial * resultat
        print(f"{initial} {source} {destination} {yes}")
    resultatFinal += yes
print(round(resultatFinal,1))

