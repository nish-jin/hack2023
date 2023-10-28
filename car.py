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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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
    
    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
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

    def set(self, file):
        nextLine = file.readline()
        v = float(nextLine)
        # read data from file ????
        # set self.voltage to represent that value
        self.voltage = v

class Car:
    def __init__(self, fileName):
        self.front = Front(0,CAR_LENGTH/2)
        self.back = Back(0,-CAR_LENGTH/2)
        self.leftfront = LeftFront(-CAR_WIDTH/2,CAR_LENGTH/2)
        self.rightfront = RightFront(CAR_WIDTH/2,CAR_LENGTH/2)
        self.rightmiddle = RightMiddle(CAR_WIDTH/2,0)
        self.leftmiddle = LeftMiddle(-CAR_WIDTH/2,0)
        self.rightback = RightBack(CAR_WIDTH/2,-CAR_LENGTH/2)
        self.leftback = LeftBack(-CAR_WIDTH/2,-CAR_LENGTH/2)
        self.position = [0, 0]
        self.brakepercentage = 0
        self.speed = 0
        self.file = open(fileName, "r")
        self.id = ""

    def getPosition(self):
        return self.position
    
    def getBrakePercentage(self):
        return self.brakepercentage

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
        nextLine = self.file.readline()
        lat = float(nextLine)

        nextLine = self.file.readline()
        long = float(nextLine)
        # read data from file ????
        # set self.voltage to represent that value
        self.position = [lat, long]
    
    def setBrakePercentage(self):
        nextLine = self.file.readline()
        percent = float(nextLine)
        # read data from file ????
        # set self.voltage to represent that value
        self.brakepercentage = percent
    
    def setSpeed(self):
        nextLine = self.file.readline()
        speed = float(nextLine)
        # read data from file ????
        # set self.voltage to represent that value
        self.speed = speed 

    def setId(self):
        nextLine = self.file.readLine()
        self.id = nextLine

    def setFront(self):
        self.front.set(self.file)

    def setBack(self):
        self.back.set(self.file)

    def setLeftFront(self):
        self.leftfront.set(self.file)

    def setRightFront(self):
        self.rightfront.set(self.file)

    def setLeftMiddle(self):
        self.leftmiddle.set(self.file)

    def setRightMiddle(self):
        self.rightmiddle.set(self.file)

    def setLeftBack(self):
        self.leftback.set(self.file)

    def setRightBack(self):
        self.rightback.set(self.file)