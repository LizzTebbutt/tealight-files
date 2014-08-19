from tealight.logo import move, turn

def spiral(size):
  
  if size > 30:
    return
  
  move(size)
  turn(90)
  spiral(size)
  
spiral(0)