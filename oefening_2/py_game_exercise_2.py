from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

for move in range(1, 10):
    robotArm.grab()
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 6):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 6):
    robotArm.moveRight()
robotArm.drop()

for moveThree in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveThree in range(1, 3):
    robotArm.moveRight()
robotArm.drop()


robotArm.wait()