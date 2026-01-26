from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 50)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)
    
t.screen.mainloop()
t.screen.bgcolor("green")