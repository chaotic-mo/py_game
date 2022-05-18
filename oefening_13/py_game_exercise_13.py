from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
hinata = 1
robotArm.grab()
while robotArm.scan() != "":
    for _ in range(hinata):
        robotArm.moveRight()
    robotArm.drop()
    hinata += 1
    for _ in range(hinata):
        robotArm.moveLeft()
    robotArm.grab()
robotArm.wait()