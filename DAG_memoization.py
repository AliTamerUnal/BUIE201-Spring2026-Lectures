
# not object oriented!!

class Node:
    def __init__(self, code: str) -> None:
        self.code = code
        
class DAG:
    def __init__(self) -> None:
         self.nodes = []
         self.arcs = []
         self.cache = {}

         self.nodes.append(Node(1))
         self.nodes.append(Node(2))         
         self.nodes.append(Node(3))

         self.arcs.append(Arc(self.nodes[0], self.nodes[1], 7))
         self.arcs.append(Arc(self.nodes[0], self.nodes[2], 10))
         self.arcs.append(Arc(self.nodes[1], self.nodes[2], 5))

    def incomming_arcs(self, v: Node):
        # Discuss performance

        inarcs = []
        for a in self.arcs:
            if (a.to_node == v):
                inarcs.append(a)
        return inarcs

    def SP(self, s : Node, v: Node) -> int:
        # Discuss performance

        min = 0
        for a in self.incomming_arcs(v):
            
            # check the cache if we had already calculated the distance from the start to the begining of arc a.
            # this is called 'memoization'. note that we only recurse if we cannot access the distance from the cache.

            distance_from_start_to_from_node_of_a = 0
            if (s, a.from_node) in self.cache.keys():
                distance_from_start_to_from_node_of_a = self.cache[(s, a.from_node)]
            else:
                distance_from_start_to_from_node_of_a = self.SP(s, a.from_node)
                self.cache[(s, a.from_node)] = distance_from_start_to_from_node_of_a

            length = a.distance + distance_from_start_to_from_node_of_a
            if (min <= 0 or length < min):
                min = length

        return min
class Arc:
    def __init__(self, from_node: Node, to_node: Node, distance: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance

d = DAG()

# Really. Not object oriented!!
print (d.SP(d.nodes[0], d.nodes[2]))






