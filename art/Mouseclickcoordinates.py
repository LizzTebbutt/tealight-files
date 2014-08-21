from tealight.art import (color, line, spot, circle, box, image, text, background)
import github.davidsamueljones.art.Minesweeper

def handle_mousemove(x,y,button):
  
  global lastx, lasty
  
  if button == "left":
    color("blue")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    
  if button == "right":
    color("red")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    
