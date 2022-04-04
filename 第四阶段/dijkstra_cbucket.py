class WDGraph(object):

    def __init__(self):

        self.maxedge = 0
        self.EdgeNumber = 0
        self.VertexNumber = 0
        self.orgin = None
        self.destn = None
        self.distance = {}  # record the min_distance
        self.adjencets = {}  # key is parent, value is a adj list

    def generate_graph(self, p, v, w):

        if self.maxedge < w:
            self.maxedge = w

        if not p in self.adjencets:
            self.adjencets.setdefault(p, [(w, v)])
        else:
            self.adjencets[p].append((w, v))

        self.adjencets.setdefault(v, [])

        self.distance.setdefault(p, None)
        self.distance.setdefault(v, None)


class LoopBucket(object):

    def __init__(self, maxedge):

        self.pointer = 0
        self.VertexNum = 0
        self.cyclebase = maxedge + 1
        self.Bucket = [[] for i in range(0, self.cyclebase)]

    def join(self, distance, parent, vertex):

        index = distance % self.cyclebase
        self.Bucket[index].append((distance, parent, vertex))
        self.VertexNum += 1

    def popmin(self):

        while not self.Bucket[self.pointer]:
            self.pointer = (self.pointer + 1) % self.cyclebase

        self.VertexNum -= 1
        return self.Bucket[self.pointer].pop()

    def isEmptyBucket(self):
        if self.VertexNum == 0:
            return True
        else:
            return False




def main():
    Graph = initial_graph()
    Bucket = LoopBucket(Graph.maxedge)
    path = []
    CurrentSet = {}  # key is vertex's name,value is its parent
    distance = 0
    parent = None
    Bucket.join(distance, parent, Graph.origin)

    while not (Graph.destn in CurrentSet.keys() and Bucket.isEmptyBucket()):
        Closest_dist, Closest_parent, Closest_name = Bucket.popmin()

        if not Closest_name in CurrentSet.keys():
            CurrentSet.setdefault(Closest_name, Closest_parent)

            # if the node has adj
            if Graph.adjencets[Closest_name]:
                for weight, adj_name in Graph.adjencets[Closest_name]:
                    distance = Closest_dist + weight

                    if Graph.distance[adj_name] is None:
                        Graph.distance[adj_name] = distance
                        parent = Closest_name
                        Bucket.join(distance, parent, adj_name)

                    elif Graph.distance[adj_name] > distance:
                        Graph.distance[adj_name] = distance
                        parent = Closest_name
                        Bucket.join(distance, parent, adj_name)

    if not Graph.destn in CurrentSet.keys():
        print("{} cannot reach {}".format(Graph.origin, Graph.destn))
    else:
        print(Graph.distance[Graph.destn])

        node = Graph.destn
        path = list()
        while not node is None:
            path.append(node)
            node = CurrentSet[node]

        path.reverse()
        print(path)


def initial_graph():
    Graph = WDGraph()

    with open('test.txt','r') as f:
        Graph.EdgeNumber = int(f.readline().strip())
        Graph.VertexNumber = int(f.readline().strip())

        for i,line in enumerate(f.readlines()):
            if  i == Graph.EdgeNumber:
                Graph.origin = line.strip()
            elif i == Graph.EdgeNumber + 1:
                Graph.destn = line.strip()
            else:
                p,v,w = line.strip().split()
                Graph.generate_graph(str(p),str(v),int(w))

        Graph.distance[Graph.origin] = int(0)

    return Graph


if __name__ == "__main__":
    main()

