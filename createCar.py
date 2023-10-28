
import json
import car
import sys

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

    # Create a JSON object w/ info 
    # a Python object (dict):
    message = {
        "front": front,
        "back": back,
        "rightFront": left_front,
        "leftFront": left_front,
        "rightMiddle": right_middle,
        "leftMiddle": left_middle,
        "rightBack": right_back,
        "leftBack": left_back,
        "position": position,
        "speed": speed,
        "brakePercentage": brake_percentage
    }

    # convert into JSON:
    return json.dumps(message)

def createCar():
    carObj = car.Car(sys.argv[1])

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

    return carObj


def main():
    return 0
        

# run main when run on command line 
if __name__ == '__main__':
    main()
        