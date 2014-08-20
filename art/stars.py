from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def circle(x, y, c, size, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (size * sin(angle))
    y0 = y + (size * cos(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

circle(300, 300, "teal", 100, 50)
circle(600, 400, "violet", 200, 100)
circle(450, 200, "gold", 125, 30)