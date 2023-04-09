class Node:
    def __init__(self):
        self.parent = None
        self.child = None
        self.value = None
        
    def __init__(self, v):
        self.parent = None
        self.child = None
        self.value = v
        
    def __repr__(self):
        return "Node({})".format(self.value)
    
    def __str__(self):
        return str(self.value)
        
    def setParent(self, p):
        self.parent = p
        
    def setChild(self, c):
        self.child = c
        
    def setValue(self, v):
        self.value = v
