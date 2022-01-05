
class Agent:
    def __init__(self, id, v, s, d, sp, g):
        self.id  =id
        self.value =v
        self.src =s
        self.dest =d
        self.speed = sp
        self.geo = g
        self.list = None
        self.pok = None

    def getId(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getPos(self):
        return self.geo

    def setPos(self, pos):
        self.geo =pos

    # def getClosest(self):
    #     return self.closest
    #
    # def setClosest(self, n):
    #     self.closes t =n

    def getList(self):
        return self.list

    def setList(self ,l):
        self.list = l

    def getPok(self):
        return self.pok

    def setPok(self ,p):
        self.pok = p

    def getSrc(self):
        return self.src

    def setSrc(self, n):
        self.src = n



    def getDest(self):
        return self.dest

    def setDest(self,n):
        self.dest=n