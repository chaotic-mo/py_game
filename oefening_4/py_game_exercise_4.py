from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for move in range(1, 3):
    robotArm.grab()
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 3):
    robotArm.moveRight()
robotArm.drop()

for moveTwo in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for moveTwo in range(1, 3):
    robotArm.moveRight()
robotArm.drop()


for moveTwo in range(1, 2):
    robotArm.grab()
    robotArm.moveLeft()
robotArm.drop()
for moveTwo in range(1, 2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
robotArm.drop()

for moveTwo in range(1, 2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
robotArm.drop()


robotArm.wait()
