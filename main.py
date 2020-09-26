from ring import HashRing
from node import Node
import random



def runTest():
    ring = HashRing(100)
    for i in range(3):
        ring.addNode(Node(i))

    print("Nodes:", len(ring.getNodes()))

    # ring.removeNode(ring.getNodes()[1])
    
    print("Nodes:", len(ring.getNodes()))

    print("\nSlot Mapping:")
    ring.printSlots()
    
    print("\nNode Mapping:")
    ring.printNodeMapping()
    
    print("\nLoads:")
    ring.printNodeLoads()

    print("\nLoad factor:")
    ring.printLoadFactor()


def runNodeAddTest():
    ring = HashRing(100, 2)
    for i in range(30):
        ring.addNode(Node(i))
        print("Nodes = ", len(ring.getNodes()), "Load = ")
        ring.printLoadFactor()

def runRebalancingFactorTest():
    ring = HashRing(100, 3)
    slots = ring.getSlots()
    print(slots)
    mapping = [slots[i] for i in range(100)]

    for i in range(100):
        if random.choice([True, True, False]):
            if (len(ring.getNodes())+1) * 3 < 100:
                print("Already present node, ", len(ring.getNodes()))
                ring.addNode(Node(i))
            else:
                continue
        else:
            if len(ring.getNodes())>1:
                ring.removeNode(ring.getNodes()[0])
            else:
                continue
        slots = ring.getSlots()
        # print(slots)
        newmapping = [slots[i] for i in range(100)]
        changes = sum([(1 if (mapping[i]!=newmapping[i]) else 0) for i in range(100)])
        print("Changed:", changes * 1.0 / len(slots))
        mapping = newmapping


        



if __name__ == '__main__':
    # runTest()
    # runNodeAddTest()
    runRebalancingFactorTest()


    


    



