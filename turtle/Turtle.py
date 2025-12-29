# https://docs.python.org/3/library/turtle.html
#yo

import turtle
import random

s = turtle.Turtle()
s.ht()

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.right(random.random()*360)
t1.fd(random.random()*100)
t2.right(random.random()*360)
t2.fd(random.random()*100)

s.screen.mainloop()
