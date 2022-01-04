

class Edges:

    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.weight = w


    def getsrc(self):
         return self.src

    def getdest(self):
        return self.dest

    def getweight(self):
        return self.weight

    def setweight(self, w):
       self.weight = w