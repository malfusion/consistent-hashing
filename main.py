from ring import HashRing
from node import Node

if __name__ == '__main__':
    ring = HashRing(100)
    for i in range(3):
        ring.addNode(Node(i))

    print("Nodes:", len(ring.getNodes()))

    # ring.removeNode(ring.getNodes()[1])
    
    print("Nodes:", len(ring.getNodes()))

    print("Slot Mapping:", ring.printSlots())
    print("Node Mapping:", ring.printNodeMapping())
    print("Load factor:", ring.getLoadFactor())
    


