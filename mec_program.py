import json
import numpy as np 
import matplotlib.pyplot as plt 

def plot(cars, objects):
    plt.title("MEC Road Representation") 
    plt.xlabel("Longtitude") 
    plt.ylabel("Latitude") 
    plt.scatter(objects[0,:], objects[1,:], color ="red")
    plt.scatter(cars[0,:], cars[1,:], color ="blue")
    plt.show()

class mec_obj:
    def __init__(self, network):
        self.message_cache = dict()
        self.mec_on = False
        self.network = network
        self.cars = np.empty([2, 0])
        self.objects = np.empty([2,0])
        self.masterlist = [] #holds all input points

    def input_message(self, message):
        '''Accepts an input message from the network.'''
        translated = json.loads(message)
        self.message_cache[translated['id']] = translated
        if self.mec_on:
            self.generate_output()
    
    def generate_output(self):
        '''Calculates global environment representation 
        and updates cars' views.'''
        self.create_cars_matrix()
        self.create_objects_matrix()
        plot(self.cars, self.objects) #plots mec (global) rep
        for k, v in self.message_cache.items():
            self.network.send_message(self.__buildJsonOutput(k), k)

    def activate_mec(self):
        '''Sets the mec to update cars in the system.'''
        self.mec_on = True
    
    def create_cars_matrix(self):
        '''Adds all car positions to the global rep.'''
        for id, data in self.message_cache.items():
            [y,x] = data["position"]
            self.cars = np.append(self.cars, [[x],[y]], axis = 1)
            self.masterlist.append([x,y])
    
    def create_objects_matrix(self):
        '''Adds all detected objects to the global rep.'''
        tempset = [] #holds all unfiltered object detection points

        #populate tempset with object detection points
        for id, data in self.message_cache.items():
            #points are relative to car that detected
            [y_base,x_base] = data["position"] 
            names = ["front","back","leftMiddle","rightMiddle","leftFront","rightFront","leftBack","rightBack"]
            for label in names:
                #for each sensor, calculate object locations where one exists
                [x,y] = data[label]
                if x != None:
                    x += x_base
                    y += y_base
                    self.masterlist.append([x,y])

                    #abandon any points within range of any known car location
                    #assume sensor detecting a car in the network
                    addVal = True
                    for i in range(len(self.cars[0])):
                        if np.abs(self.cars[0,i] - x) <= 2:
                            if np.abs(self.cars[1,i] - y) <= 2:
                                addVal = False
                                break
                    if addVal:
                        tempset.append([x,y])
        
        #clean and save obj locations
        self.__clean_obj_matrix(tempset)

    def __clean_obj_matrix(self, objset):
        '''Finds groups of object points and averages 
        them as a single object.'''
        clusters = []

        #generate data groups within 'clusters'
        while len(objset) != 0:
            clusters.append([])
            clusters[-1].append(objset.pop())

            addIndex = 0
            #loop until no points are close enough to add
            while addIndex != -1:
                addIndex = -1
                #search for next point to add
                for i in range(len(objset)):
                    #objset is [[x,y], ...] - clusters is [ [[x,y], ...], [...], ...]
                    if np.abs(objset[i][0] - clusters[-1][0][0]) <= 4:
                        if np.abs(objset[i][1] - clusters[-1][0][1]) <= 4:
                            addIndex = i
                            break
                if addIndex >= 0:
                    clusters[-1].append(objset.pop(addIndex))

        #average the points in each data group and make the object list
        for group in clusters:
            temp = np.mean(group, axis = 0).reshape(-1,1)
            self.objects = np.append(self.objects, temp, axis=1)

    def __buildJsonOutput(self, id):
        '''Builds a JSON message to be sent to specified car.'''
        message = self.message_cache[id] 

        #construct list of objects (incl. cars) relevant to specified car
        relativeData = []
        y = message["position"][0]
        x = message["position"][1]
        for i in range(len(self.cars[0])):
            x_curr = self.cars[0,i]
            y_curr = self.cars[1,i]
            if np.abs(x_curr - x) <= 150 and (x != x_curr or y != y_curr):
                relativeData.append((x_curr-x,y_curr-y))

        for i in range(len(self.objects[0])):
            x_curr = self.objects[0,i]
            y_curr = self.objects[1,i]
            if np.abs(x_curr - x) <= 150:
                relativeData.append((x_curr-x,y_curr-y))

        return json.dumps({"data":relativeData})
        
        


            
            