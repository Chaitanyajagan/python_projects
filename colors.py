import turtle
import time
import random

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define the cube vertices
vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
]

# Define the cube edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define the colourful patterns
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to draw a line
def draw_line(x1, y1, z1, x2, y2, z2, colour):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(colour)
    t.goto(x2, y2)

# Function to rotate the cube
def rotate_cube(angle):
    for edge in edges:
        v1, v2 = vertices[edge[0]], vertices[edge[1]]
        x1, y1, z1 = v1
        x2, y2, z2 = v2
        draw_line(x1, y1, z1, x2, y2, z2, random.choice(colours))
    t.right(angle)

# Main loop
while True:
    rotate_cube(5)
    time.sleep(0.05)

# Keep the window open
win.mainloop()
