from tealight.logo import move, turn

def spiral(size):
  
  if size > 70:
    return
  
  move(size)
  turn(90)
  spiral(size + 5)
  
spiral(0)