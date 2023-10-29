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
        self.masterlist = set()

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
                        if x-2 <= self.cars[0,i]  <= x+2:
                            if y-2 <= self.cars[1,i] <= y-2:
                                addVal = False
                                break
                    if addVal:
                        self.objects = np.append(self.objects, [[x],[y]], axis = 1)




            
