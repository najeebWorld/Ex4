class Pokemon:
    def __init__(self, t,v,pos):
        self.type=t
        self.value=v
        self.geo=pos
        self.edge=None
    def __repr__(self):
        t=str(self.type)
        v=str(self.value)
        g1=str(self.geo[0])
        g2 = str(self.geo[1])
        g3 = str(self.geo[2])
        e=str(self.edge)

        return "Pokemon= type: "+t+" value: "+v+" geo: ("+g1+","+g2+","+g3+")"+"edge: "+e

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def getPos(self):
        return self.geo

    def getEdge(self):
        return self.edge

    def setEdge(self,e):
        self.edge=e