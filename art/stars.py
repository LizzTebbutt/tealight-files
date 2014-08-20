from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = y + (size * cos(angle))
    y0 = x + (size * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

star(300, 300, "teal", 100, 50)
star(600, 400, "violet", 200, 100)
star(450, 200, "gold", 125, 30)