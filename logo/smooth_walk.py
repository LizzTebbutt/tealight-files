from tealight.logo import (move, turn,
                           pen_down, pen_up,
                           show_turtle, hide_turtle,
                           color, speed)

from random import random

i = 0

while i < 10000:
  print i
  color("hsl(%d,60%%,50%%)" % i)
  i += 1

def handle_mousedown(x,y):
  global d
  d = 0
 
d = int(random()*360)

def handle_frame():
  global d
  
  for x in range(10):
    d+=1
    
    color("hsl(%d,100%%,50%%)" % d)
    move(random()*5)
    turn(random()*90 - 45)