from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for Bigmove in range(5):
    for moveX in range(6):
        robotArm.moveRight()    
        robotArm.grab()   
        robotArm.moveLeft()
        robotArm.drop()
    for moveXX in range(2):
        robotArm.moveRight()
robotArm.wait()