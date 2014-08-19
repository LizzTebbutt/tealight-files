from tealight.logo import move, turn


def polygon(side):
  for i in range(0,4):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    polygon(decoration)
    turn(angle)

turn(-90)
waterwheel(20,75)
