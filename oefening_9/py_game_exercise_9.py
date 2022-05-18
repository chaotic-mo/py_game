from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for _ in range(14):
    robotArm.grab()
    if robotArm.scan() == "":
        robotArm.moveRight()
    for _ in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for _ in range(5):
        robotArm.moveLeft()   
robotArm.wait()