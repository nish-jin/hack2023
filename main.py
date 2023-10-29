
import json
import car
import sys
import fiveG_simulator
import mec_program
import numpy as np 
import matplotlib.pyplot as plt 

def getJson(carObj):
    # call functions to retrieve the new sensor values
    front = carObj.getFront()
    back = carObj.getBack()
    left_front = carObj.getLeftFront()
    left_middle = carObj.getLeftMiddle()
    left_back = carObj.getLeftBack()
    right_front = carObj.getRightFront()
    right_middle = carObj.getRightMiddle()
    right_back = carObj.getRightBack()
    speed = carObj.getSpeed()
    position = carObj.getPosition()
    brake_percentage = carObj.getBrakePercentage()
    id = carObj.getId()

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
    return json.dumps(message)

def createCar(fileName):
    carObj = car.Car(fileName)

    # call functions to tell sensors to read new values
    carObj.setFront()
    carObj.setBack()
    carObj.setLeftFront()
    carObj.setLeftMiddle()
    carObj.setLeftBack()
    carObj.setRightFront()
    carObj.setRightMiddle()
    carObj.setRightBack()
    carObj.setSpeed()
    carObj.setPosition()
    carObj.setBrakePercentage()
    carObj.setId()

    return carObj

def plot(cars, objects):
    plt.title("Car graph") 
    plt.xlabel("X axis") 
    plt.ylabel("Y axis") 
    plt.scatter(objects[0,:], objects[1,:], color ="red")
    plt.scatter(cars[0,:], cars[1,:], color ="green")
    plt.show()

def main():
    #setup environment
    network = fiveG_simulator.fiveG_Network()
    mec_calculator = mec_program.mec_obj(network)
    network.ping('mec', mec_calculator)

    file = open(sys.argv[1], "r")
    nextLine = file.readline()
    car_list = list()
    while nextLine != "":
        #build, add, and broadcast from car
        car_list.append(createCar(nextLine.strip()))
        network.ping((car_list[-1]).getId, car_list[-1])
        jsonMessage = getJson(car_list[-1])
        network.broadcast(jsonMessage)
        
        nextLine = file.readline()

    mec_calculator.create_cars_matrix()
    mec_calculator.create_objects_matrix()
    print(mec_calculator.message_cache)

    plot(mec_calculator.cars, mec_calculator.objects)

    mec_calculator.activate_mec()
    #TODO re-send a car message
    # for k, v in mec_calculator.message_cache.items():
    #     print(mec_calculator.findRelevantData(k))




# run main when run on command line 
if __name__ == '__main__':
    main()
        