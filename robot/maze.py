from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

#move forwards until you can't move any more
#if a wall is hit, check the left side for a wall
#if there is a wall to the left, turn left and check again
#move again

while touch() !="fruit":

  while touch() != 'wall':
    move()
  
  if touch() == 'wall':
    turn(1)
  
    if touch()=='wall':
      turn(2)
  
  
  