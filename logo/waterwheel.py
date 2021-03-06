from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(120)

def waterwheel(edges, size):
  angle = 400 / edges
  decoration = size / 6
  for i in range(0, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)                                 #rotates around central pivot
waterwheel(20,200)                        #size of waterwheel
