

class Node():
    def __init__(self, id):
        super().__init__()
        self.id = id

    def getId(self):
        return self.id

    def __repr__(self):
        return super().__repr__() + ("{ NodeID: %d }" %(self.id))
