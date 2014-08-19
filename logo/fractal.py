from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

# Draws the von Koch Snowflake curve

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    turn(120)
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    

turn(90)
move(-300)
segment(600,6)
move(-300)