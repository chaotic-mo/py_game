from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
amangus = 9
for _ in range(5):
    robotArm.grab()
    for _ in range(amangus):
        robotArm.moveRight()
    robotArm.drop()
    amangus -= 1
    for _ in range(amangus):
        robotArm.moveLeft()
    amangus -= 1
robotArm.wait()