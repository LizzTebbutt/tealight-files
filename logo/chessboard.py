from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)

turn(90)    
move(40)
    
   
polygon(4,400)