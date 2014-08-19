from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
    turn(180)    
    move(40)
    turn(180)
    move(400)
    
   
polygon(4,400)