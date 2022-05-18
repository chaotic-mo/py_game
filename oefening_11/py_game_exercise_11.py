from RobotArm import RobotArm
robotArm = RobotArm('exercise 11') 
right = 10
for _ in range(right):
    robotArm.moveRight()
for _ in range(right):
    robotArm.moveLeft()
    right -= 1
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "white":
        robotArm.moveRight()
    robotArm.drop()
robotArm.wait()