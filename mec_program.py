import json
import numpy as np 
import matplotlib.pyplot as plt 

class mec_obj:
    def __init__(self, network):
        self.message_cache = dict()
        self.mec_on = False
        self.network = network
        self.cars = np.empty([2, 0])
        self.objects = np.empty([2,0])
        self.masterlist = []

    def input_message(self, message):
        #TODO check json name is right
        translated = json.loads(message)
        self.message_cache[translated['id']] = translated
        if self.mec_on:
            self.generate_output()
    
    def generate_output(self):
        #TODO calc responses and use self.network.send_message()
        return 0
    
    def create_cars_matrix(self):
        for id, data in self.message_cache.items():
            [y,x] = data["position"]
            self.cars = np.append(self.cars, [[x],[y]], axis = 1)
            self.masterlist.append([x,y])
    
    def create_objects_matrix(self):
        tempset = []
        for id, data in self.message_cache.items():
            [y_base,x_base] = data["position"]
            names = ["front","back","leftMiddle","rightMiddle","leftFront","rightFront","leftBack","rightBack"]
            for label in names:
                [x,y] = data[label]
                if x != None:
                    x += x_base
                    y += y_base
                    self.masterlist.append([x,y])

                    addVal = True
                    for i in range(len(self.cars[0])):
                        if np.abs(self.cars[0,i] - x) <= 2:
                            if np.abs(self.cars[1,i] - y) <= 2:
                                addVal = False
                                break
                    if addVal:
                        #self.objects = np.append(self.objects, [[x],[y]], axis = 1)
                        tempset.append([x,y])
            
        self.clean_obj_matrix(tempset)

    def clean_obj_matrix(self, objset):
        clusters = []

        #generate clusters within clusters
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

        #average the points in each cluster and make the object list
        for cluster in clusters:
            temp = np.mean(cluster, axis = 0).reshape(-1,1)
            self.objects = np.append(self.objects, temp, axis=1)

    def findRelevantData(self, id):
        message = self.message_cache[id] 

        relativeData = []
        y = message["position"][0]
        x = message["position"][1]
        for i in range(len(self.cars[0])):
            x_curr = self.cars[0,i]
            y_curr = self.cars[1,i]
            if np.abs(x_curr - x) <= 150 and (x != x_curr or y != y_curr):
                relativeData.append((x_curr,y_curr))

        for i in range(len(self.objects[0])):
            x_curr = self.objects[0,i]
            y_curr = self.objects[1,i]
            if np.abs(x_curr - x) <= 150:
                relativeData.append((x_curr,y_curr))

        return relativeData
        
        


            
            