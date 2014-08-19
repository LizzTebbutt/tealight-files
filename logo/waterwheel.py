from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 4
  for i in range(0, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)                                 #rotates around central pivot
waterwheel(20,200)                        #size of waterwheel
