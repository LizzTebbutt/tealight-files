from tealight.art import (color, line, spot, circle, box, image, text, background)

for x in range(0,540):
  for y in range(0,390):

    if y > x*x:
      color("red")
    elif y > x:
      color("green")
    elif y*y < x:
      color("yellow")
    else:
      color("blue")
    
    box(x,y,10,10)