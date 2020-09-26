from ring import HashRing
from node import Node

if __name__ == '__main__':
    ring = HashRing(100)
    for i in range(10):
        ring.addNode(Node(i))

    print("Nodes:", len(ring.getNodes()))

    ring.removeNode(ring.getNodes()[5])
    
    print("Nodes:", len(ring.getNodes()))
    


