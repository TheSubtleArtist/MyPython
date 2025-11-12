#
#  Robot Control Map
#
#  +-------------------+
# 9|                   |
# 8|S                  |
# 7|            x x x x|
# 6|            x      |
# 5|            x F    |
# 4|                   |
# 3|                   |
# 2|                   |
# 1|                   |
# 0|                   |
#  +-------------------+
#   0 1 2 3 4 5 6 7 8 9
#
#  S = Start position (0,8) F = Target destination (7,5),
#  x = Ravine, robot will be lost if hits these coords
#
# import robot module and use the robot.left(), robot.right(),
# robot.up() and robot.down() functions
#
import robot


for a in range(4):
  robot.down()
  
for b in range(7):
  robot.right()

for c in range(1):
  robot.up()