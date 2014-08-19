from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["lemon", "orange", "gold", "burgundy", "teal", "indigo", "brown"]

for i in range(0,1000):
  move(i)
  turn(200)
  color(colors[i%7])