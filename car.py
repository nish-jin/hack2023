# import math for sin and cos
import math
import json
import numpy as np 
import matplotlib.pyplot as plt 
CAR_WIDTH = 1
CAR_LENGTH = 1
THETA = 45

def distance(voltage):
    return (5 - voltage) * 398.0 / 5

class Front:
    def __init__(self,x,y):
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
        self.voltage = v

class Back:
    def __init__(self,x,y):
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
        self.voltage = v

class LeftFront:
    def __init__(self,x,y):
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
        self.voltage = v

class RightFront:
    def __init__(self,x,y):
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
        self.voltage = v

class RightMiddle:
    def __init__(self,x,y):
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
        self.voltage = v

class LeftMiddle:
    def __init__(self,x,y):
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
        self.voltage = v

class RightBack:
    def __init__(self,x,y):
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
        self.voltage = v

class LeftBack:
    def __init__(self,x,y):
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
        self.voltage = v

class Car_mock:
    '''Simulates the data and behavior expected of a car in the network.'''
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
        self.id = 0
        self.data = np.empty([2,0])

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
    
    def getId(self):
        return self.id

    def setPosition(self):
        #Converting from gps to cm
        nextLine = self.file.readline()
        lat = float(nextLine)
        lat = lat / 360 * 2 * math.pi * 637800000

        nextLine = self.file.readline()
        long = float(nextLine)
        long = long / 360 * 2 * math.pi * 637800000
        self.position = [lat, long]
    
    def setBrakePercentage(self):
        nextLine = self.file.readline()
        percent = float(nextLine)
        self.brakepercentage = percent
    
    def setSpeed(self):
        nextLine = self.file.readline()
        speed = float(nextLine)
        self.speed = speed 

    def setId(self):
        nextLine = self.file.readline()
        id = int(nextLine)
        self.id = id

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

    def sendJson(self, network_connection):
        '''Generates a JSON brodcast message for the given Car.'''
        # call functions to retrieve the new sensor values
        front = self.getFront()
        back = self.getBack()
        left_front = self.getLeftFront()
        left_middle = self.getLeftMiddle()
        left_back = self.getLeftBack()
        right_front = self.getRightFront()
        right_middle = self.getRightMiddle()
        right_back = self.getRightBack()
        speed = self.getSpeed()
        position = self.getPosition()
        brake_percentage = self.getBrakePercentage()
        id = self.getId()

        # Create a JSON object w/ info 
        # a Python object (dict):
        message = {
            "front": front,
            "back": back,
            "rightFront": right_front,
            "leftFront": left_front,
            "rightMiddle": right_middle,
            "leftMiddle": left_middle,
            "rightBack": right_back,
            "leftBack": left_back,
            "position": position,
            "speed": speed,
            "brakePercentage": brake_percentage,
            "id": id
        }

        # convert into JSON:
        network_connection.broadcast(json.dumps(message))
    
    def input_message(self, message):
        '''Accepts an input message from the network.'''
        #convert JSON to py type
        translated = json.loads(message)

        #extract object data from message and construct visual rep
        for coord in translated["data"]:
            x = coord[0]
            y = coord[1]
            self.data = np.append(self.data, [[x],[y]], axis=1)
        title = "Car ID " + str(self.id) + ": Road Graph"
        plt.title(title) 
        plt.xlabel("Longitude") 
        plt.ylabel("Latitude") 
        plt.scatter([0], [0], color = "blue")
        plt.scatter(self.data[0,:], self.data[1,:], color ="red")
        plt.xlim(-150,150)
        plt.annotate("You", (2, 2))
        plt.show()
