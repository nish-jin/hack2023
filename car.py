

def distance(voltage):
    return voltage * 398.0 / 5

Class Front:
    __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        return [self.x+0,self.y+distance(self.voltage)]

    def set(self):
        # read data from file ????
        # set self.voltage to represent that value

Class car:
    __init__(self):
        self.front = Front(0,1)
        self.back = Back(0,-1)
        self.leftFront = LeftFront(-1,1)
        self.rightFront = RightFront(1,1)
        self.rightMiddle = RightMiddle(1,0)
        self.leftMiddle = LeftMiddle(-1,0)
        self.rightBack = RightBack(1,-1)
        self.leftBack = LeftBack(-1,-1)

    def getFront(self):
        return self.front.get()

    def getBack(self):
        return self.back.get()

    def getLeftFront(self):
        return self.leftfront.get()

    def getRightFront(self):
        return self.rightfront.get()

    def getLeftMiddle(self):
        return self.leftmiddle.get()

    def getRightMiddle(self):
        return self.rightmiddle.get()

    def getLeftBack(self):
        return self.leftback.get()

    def getRightBack(self):
        return self.rightback.get()

    def setFront(self):
        self.front.set()

    def setBack(self):
        self.back.set()

    def setLeftFront(self):
        self.leftfront.set()

    def setRightFront(self):
        self.rightfront.set()

    def setLeftMiddle(self):
        self.leftmiddle.set()

    def setRightMiddle(self):
        self.rightmiddle.set()

    def setLeftBack(self):
        self.leftback.set()

    def setRightBack(self):
        self.rightback.set()