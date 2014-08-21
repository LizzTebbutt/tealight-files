from tealight.art import (color, line, spot, circle, box, image, text, background)

  if button == "left":
    color("blue")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
