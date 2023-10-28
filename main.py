
import json

def main():
    car = Car()

    while(1):
        # call functions to tell sensors to read new values
        car.setFront()
        car.setBack()
        car.setLeftFront()
        car.setLeftMiddle()
        car.setLeftBack()
        car.setRightFront()
        car.setRightMiddle()
        car.setRightBack()
        car.setSpeed()
        car.setPosition()
        car.setBrakePosition()

        # call functions to retrieve the new sensor values
        front = car.getFront()
        back = car.getBack()
        left_front = car.getLeftFront()
        left_middle = car.getLeftMiddle()
        left_back = car.getLeftBack()
        right_front = car.getRightFront()
        right_middle = car.getRightMiddle()
        right_back = car.getRightBack()
        speed = car.getSpeed()
        position = car.getPosition()
        brake_percentage = car.getBrakePosition()

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
        send = json.dumps(message)

        