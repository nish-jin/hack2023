
import car
import sys
import fiveG_simulator
import mec_program
import numpy as np 
import matplotlib.pyplot as plt 

def createCar(fileName):
    '''Builds a car object using an input file.'''
    carObj = car.Car_mock(fileName)

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

def main():
    #setup network environment
    network = fiveG_simulator.fiveG_Network()
    mec_calculator = mec_program.mec_obj(network)
    network.ping('mec', mec_calculator)

    #setup all the cars using a formatting file
    file = open(sys.argv[1], "r")
    nextLine = file.readline()
    car_list = list()
    while nextLine != "":
        #build, add, and broadcast from car
        car_list.append(createCar(nextLine.strip()))
        network.ping((car_list[-1]).getId(), car_list[-1])
        car_list[-1].sendJson(network)
        
        nextLine = file.readline()

    #re-send a car message to prompt response from active mec
    mec_calculator.activate_mec()
    car_list[-1].sendJson(network)


# run main when run on command line 
if __name__ == '__main__':
    main()
        