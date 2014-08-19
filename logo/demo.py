from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "orange", "gold", "lime", "cyan", "indigo", "violet"]

for i in range(0,2000):
  move(i)
  turn(187)
  color(colors[i%7])