x = 30
class Telephone:
    def __init__(self, ringtone = "ringtone"):
        self.ringtone = ringtone
        print ("Telephone created with ringtone: " + self.ringtone)

    def Respond():
        pass
    def Ring(self):
        print (self.ringtone)



t1 = Telephone("ringtone1") #implicitly calls Telephone.__init__(created object, "ringtone1")
t5 = t1
t1.Ring() #Telephone.Ring(t1)
t2 = Telephone("ringtone2")
t2.Ring() #Telephone.Ring(t2)


class Node:
    def __init__(self, id):
        self.id = id

Nodes = [Node(1), Node(2), Node(3), Node(4)]

print (Nodes[0].id)

for i in range(1000):
    Nodes.append(Node(i+5))

for node in Nodes:
    print (node.id) 


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

g = Graph(Nodes)