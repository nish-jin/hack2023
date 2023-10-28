# import math for sin and cos
import math

CAR_WIDTH = 1
CAR_LENGTH = 1
THETA = 45

def distance(voltage):
    return (5 - voltage) * 398.0 / 5

class Front:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x+0,self.y+distance(self.voltage)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class Back:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x+0,self.y-distance(self.voltage)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class LeftFront:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x-distance(self.voltage)*math.cos(THETA * math.pi / 180),self.y+distance(self.voltage)*math.sin(THETA * math.pi / 180)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class RightFront:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x+distance(self.voltage)*math.cos(THETA * math.pi / 180),self.y+distance(self.voltage)*math.sin(THETA * math.pi / 180)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class RightMiddle:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x+distance(self.voltage),0]
    
    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class LeftMiddle:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x-distance(self.voltage),0]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class RightBack:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x+distance(self.voltage)*math.cos(THETA * math.pi / 180),self.y-distance(self.voltage)*math.sin(THETA * math.pi / 180)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class LeftBack:
    # TODO: Update
    def __init__(self,x,y):
        #self.object = False
        self.voltage = 0
        self.x = x
        self.y = y

    def get(self):
        if self.voltage == 0:
            return [None, None]
        return [self.x-distance(self.voltage)*math.cos(THETA * math.pi / 180),self.y-distance(self.voltage)*math.sin(THETA * math.pi / 180)]

    def set(self):
        v = 0
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class Car:
    def __init__(self):
        self.front = Front(0,CAR_LENGTH/2)
        self.back = Back(0,-CAR_LENGTH/2)
        self.leftFront = LeftFront(-CAR_WIDTH/2,CAR_LENGTH/2)
        self.rightFront = RightFront(CAR_WIDTH/2,CAR_LENGTH/2)
        self.rightMiddle = RightMiddle(CAR_WIDTH/2,0)
        self.leftMiddle = LeftMiddle(-CAR_WIDTH/2,0)
        self.rightBack = RightBack(CAR_WIDTH/2,-CAR_LENGTH/2)
        self.leftBack = LeftBack(-CAR_WIDTH/2,-CAR_LENGTH/2)
        self.position = [0, 0]
        self.brakePercentage = 0
        self.speed = 0

    def getPosition(self):
        return self.position
    
    def getBrakePercentage(self):
        return self.brakePercentage

    def getSpeed(self):
        return self.speed

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

    def setPosition(self):
        # TODO: File thing
        return 0
    
    def setBrakePercentage(self):
        # TODO: File thing
        return 0
    
    def setSpeed(self):
        # TODO: File thing
        return 0

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