from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "orange", "gold", "lime", "teal", "indigo", "violet"]

for i in range(0,1000):
  move(i)
  turn(200)
  color(colors[i%7])