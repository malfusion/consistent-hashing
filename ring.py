from node import Node

class HashRing():
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.nodes = []
        self.slotMapping = {}
        pass


    def addNode(self, node):
        print("Adding Node", node)
        self.nodes.append(node)

    
    def removeNode(self, node):
        print("Removing Node", node)
        self.nodes.remove(node)

    def getNodes(self):
        return self.nodes