

class Agent:
    def __init__(self, id, g, s):
        self.id=id
        self.geo=g
        self.speed=s
        self.closest=None
        self.list=None
        self.pok=None

    def getId(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getLoction(self):
        return self.geo

    def setLocation(self, pos):
        self.geo=pos

    def getClosest(self):
        return self.closest

    def setClosest(self, n):
        self.closest=n

    def getList(self):
        return self.list

    def setList(self,l):
        self.list=l

    def getPok(self):
        return self.pok

    def setPok(self,p):
        self.pok=p
