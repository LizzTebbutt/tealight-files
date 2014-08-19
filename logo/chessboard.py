from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    
move(50)
turn(90)
move(50)
turn(270)
move(50)
turn(90)
move(50)
    
polygon(4,50)