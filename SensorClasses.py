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

        # call functions to retrieve the new sensor values
        front = car.getFront()
        back = car.getBack()
        leftfront = car.getLeftFront()
        leftmiddle = car.getLeftMiddle()
        leftback = car.getLeftBack()
        rightfront = car.getRightFront()
        rightmiddle = car.getRightMiddle()
        rightback = car.getRightBack()

        # Create a JSON object w/ info
