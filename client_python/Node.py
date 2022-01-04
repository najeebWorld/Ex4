class Node:

    # def __init__(self, x: int =None , y: int= None, z: int=None , id: int=None ):
    #     self.x = x
    #     self.y = y
    #     self.z = z
    #     self.id = id
    #     self.in1 = dict()
    #     self.out1 = dict()
    #     self.tag = 0

    def __init__(self, pos: tuple = None, id: int = None):
        self.pos = pos
        self.id = id
        self.in1 = dict()
        self.out1 = dict()
        self.tag = 0

    def __repr__(self):
        out =" |edges out| "
        in2 =" |edges in| "
        inlen=len(self.in1)
        outlen=len(self.out1)
        id=self.id
        strin=str(inlen)
        strout=str(outlen)
        strid=str(id)
        return strid+":"+out+strout+in2+strin





        # this function returns the id
    def getId(self):
        return self.id

    # this function returns the pos
    def getPos(self):
        return self.pos

    # this function sets the pos
    def setPos(self, tup):
        self.pos=tup

        # this function returns the x
    def getX(self):
        x=self.pos[0]
        return x

        # this function returns the y
    def getY(self):
        y=self.pos[1]
        return y

        # this function returns the y
    def getZ(self):
        z= self.pos[2]
        return z

    #     # this function set new value of x
    # def setX(self,x):
    #    self.x = x
    #
    #     # this function set new value of y
    # def setY(self,y):
    #     self.y = y
    #
    #     # this function set new value of x
    # def setZ(self,z):
    #     self.z = z

         #this function return the dictionary of nodes in
    def getIn1(self):
        return self.in1

        # this function return the dictionary of nodes out
    def getOut1(self):
        return  self.out1


    def gettag(self):
        return self.tag


    def settag(self,t):
        self.tag=t;







