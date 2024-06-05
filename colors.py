from turtle import *
import turtle 
colors=['orange','red','pink','yellow','blue','green']
for x in range(50):
    pencolor(colors[x%6])
    width(x/5+1)
    forward(x)
    left(20)
turtle.done()