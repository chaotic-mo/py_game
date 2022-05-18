from timeit import repeat
from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')
for move in range(1, 2):
    robotArm.grab()
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 2):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 2):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 2):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

robotArm.wait()