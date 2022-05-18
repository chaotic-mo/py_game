from timeit import repeat
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
# Jouw python instructies zet je vanaf hier:

for move in range(1, 8):
    robotArm.moveRight()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()

for move in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 2):
    robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()