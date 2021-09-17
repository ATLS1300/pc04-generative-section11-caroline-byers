'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME GOES HERE <----------
May 29, 2020

PROGRAM DESCRIPTION GOES HERE <---------
'''
import turtle #import the library of commands that you'd like to use
import math #get a bunch of math commands

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#=======Add your code here======

panel.bgcolor("white") # set background color
#turtle.tracer(0) # turn off the animation  #uncomment along with line 33. ALWAYS update the panel!

turtle.Turtle(visible=False) # create a turtle, make it invisible 

#===================
# YOUR CODE HERE!
#polygon spirograph 
turtle.up()
turtle.speed(10)
turtle.goto(0,40)
turtle.down()
turtle.color(135,206,250) 

size = 30
sides = 12 # chage this to change the shape!
angle = 360/sides

inc = 15 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 10 # radius of inner circle

for iteration2 in range(numIt):
    turtle.down()
    for iteration1 in range(sides):
        turtle.forward(size)
        turtle.right(angle)
    turtle.up()
    turtle.forward(innerCirc)
    turtle.right(inc)
 
#ellipse
turtle.up()

scale = 10
radiusX = 30
radiusY = 10
    
y = scale * math.sin(0)*radiusY
x = scale * math.cos(0)*radiusX
turtle.goto(x,y)
turtle.color(0,0,0)

scale = 10
radiusX = 30
radiusY = 10

turtle.down()

for angle in range(360):
    y = scale * math.sin(angle)*radiusY
    x = scale * math.cos(angle)*radiusX
    turtle.goto(x,y)


    




#panel.update() # if the animation is off (line 25 is uncommented), then uncomment this line.
#===================
# turtle.done()
