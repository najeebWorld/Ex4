

class Pokemon:
    def __init__(self, t,v,pos):
        self.type=t
        self.value=v
        self.geo=pos
        self.edge=None


    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def getGeo(self):
        return self.geo

    def getEdge(self):
        return self.edge

    def setEdge(self,e):
        self.edge=e

