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
    
    def create_objects_matrix(self):
        for id, data in self.message_cache.items():
            [y_base,x_base] = data["position"]
            names = ["front","back","leftMiddle","rightMiddle","leftFront","rightFront","leftBack","rightBack"]
            for label in names:
                [x,y] = data[label]
                if x != None:
                    x += x_base
                    y += y_base
                    self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["back"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["leftMiddle"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["rightMiddle"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["leftFront"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["rightFront"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["leftBack"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            # [x,y] = data["rightBack"]
            # x += x_base
            # y += y_base
            # if x != None:
            #     self.objects = np.append(self.objects, [[x],[y]], axis = 1)
            
            
