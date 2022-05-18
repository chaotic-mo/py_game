from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
for x in range(10, 1, -1):
    robotArm.grab()
    if robotArm.scan() != "red":
            robotArm.drop()
            robotArm.moveRight()
    if robotArm.scan() == "red":
        for x in range(x):
            robotArm.grab()
            robotArm.moveRight()
        robotArm.drop()
        for x in range(x -1):
            robotArm.moveLeft()
robotArm.wait()















#try 5
# for _ in range(2):
#     for _ in range(9):
#         robotArm.moveRight()
#     for _ in range(10):
#         robotArm.moveLeft()
#         robotArm.grab()
#         robotArm.scan()
#         if robotArm.scan() == "red":
#             for _ in range(10):
#                 robotArm.moveRight()
#             robotArm.drop()
#         if robotArm.scan() != "red":
#             robotArm.drop()

