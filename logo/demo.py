from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["purple", "gold", "teal", "orange"]

for i in range(0,2000):
  move(i)
  turn(300)
  color(colors[i%3])