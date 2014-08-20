from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0.1981
t=0.1

power = 0.3

def handle_keydown(key):
  global ax, ay 
  
  if key == "left":
    ax = -power + (power*(0.9^power))
  elif key == "right":
    ax = power - (power*(0.9^power))
  elif key == "up":
    ay = -power + (power*(0.9^power))
  elif key == "down":
    ay = power - (power*(0.9^power))

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  if 1020 < y:
    vy=-vy
  elif y < 1:
    vy=-vy
    
    
  if 910 < x:
    vx=-vx  
  elif x < 1:
    vx=-vx
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)