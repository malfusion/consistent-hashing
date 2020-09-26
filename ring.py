from node import Node
from collections import Counter

class HashRing():
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.nodes = []
        self.slotMapping = {}
        self.nodePositions = []
        pass


    def addNode(self, node):
        print("Adding Node", node)
        self.nodes.append(node)
        self.recalculateSlotMapping()

    
    def removeNode(self, node):
        print("Removing Node", node)
        self.nodes.remove(node)

    def getHash(self, key):
        return hash(key) % self.capacity

    def recalculateSlotMapping(self):

        occupied = set([])
        nodePositions = []
        for node in self.nodes:
            nodeId = str(node.getId())

            
            hashAttempt = 0
            pos = self.getHash(nodeId + '_' + str(hashAttempt))
            while pos in occupied:
                print("Node", node, "experienced ", str(hashAttempt), "th hash conflict. Trying alternate hash.")
                hashAttempt += 1
                pos = self.getHash(nodeId + '_' + str(hashAttempt))
            
            nodePositions.append((pos, node))
            occupied.add(pos)
                    
        self.nodePositions = sorted(nodePositions, key = lambda x: x[0])


        currNode = 0

        self.slotMapping = {}
        for i in range(self.capacity):
            self.slotMapping[i] = self.nodePositions[currNode][1]
            if i == self.nodePositions[currNode][0]:
                currNode += 1
                # If reached the last Node Position, then map all future positions to the Zeroth node position.
                if currNode == len(self.nodePositions):
                    currNode = 0


    def printSlots(self):
        for i in range(self.capacity):
            print("Slot", i, ":", "Node", self.slotMapping[i].getId())

    
    def getLoadFactor(self):
        ctr = Counter()
        for i in range(self.capacity):
            ctr[self.slotMapping[i].getId()] += 1
        print(ctr)

    def printNodeMapping(self):
        for nodePos in self.nodePositions:
            print("Pos", nodePos[0], ":", "Node", nodePos[1].getId())


    def getNodes(self):
        return self.nodes