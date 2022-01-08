
class Agent:
    def __init__(self, id, v, s, d, sp, g):
        self.id  =id
        self.value =v
        self.src =s
        self.dest =d
        self.speed = sp
        self.geo = g
        self.pok = None


    def __repr__(self):
        i=str(self.id)
        v = str(self.value)
        s=str(self.src)
        d=str(self.dest)
        sp=str(self.speed)
        g1 = str(self.geo[0])
        g2 = str(self.geo[1])
        g3 = str(self.geo[2])
        p=str(self.pok)

        return " Agent = id: "+i+" value: "+v+" src: " +s+" dest: "+d+" speed: "+sp +" geo: ("+g1+","+g2+","+g3+")"+" pok: "+p

    def getId(self):
        return self.id

    def getSpeed(self):
        return self.speed

    def getPos(self):
        return self.geo

    def setPos(self, pos):
        self.geo =pos


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