from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["purple", "gold", "teal"]

for i in range(0,2000):
  move(i)
  turn(120)
  color(colors[i%3])