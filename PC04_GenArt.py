"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Caroline Byers

********* HEY, READ THIS FIRST **********

My code creates an illustration of some trees and flowers. I didnt want to 
make it that realistic, but rather use funky colors and shapes to represent the flowers, 
trees and sky. The colors make me happy and it should evoke a warm feeling of happiness
when you see it! 
"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#triangle 1 that is a tree
panel=turtle.Screen().bgcolor("plum1")
triangle = turtle.Turtle()
triangle.speed(10)
triangle.up()
triangleColors = ("DarkViolet","MediumOrchid","Orchid","Violet","DarkMagenta","Purple")
#colors of tree are random because they change colors 

triangle.goto(-250,-250)
triangle.down()
triangle.color(random.choice(triangleColors))
triangle.begin_fill()

#this loop creates the tree
yval = -250 

for i in range(22):
    triangle.goto(-250,yval)
    for i in range(3):
        triangle.forward(100)
        triangle.left(120)
        yval += 7    
        
triangle.end_fill()
triangle.up()
    
#triangle 2 that is a tree
triangle2 = turtle.Turtle()
triangle2.speed(10)
triangle2.up()
triangle2Colors=("PaleGreen","PaleGreen2","chartreuese")
#colors are random becuase trees change colors 

triangle2.color(random.choice(triangle2Colors))


triangle2.goto(165,-250)
triangle2.down()
triangle2.color(random.choice(triangle2Colors))
triangle2.begin_fill()

#this loop creates the 2nd tree
yval = -250 

for i in range(7):
    triangle2.goto(165,yval)
    for i in range(3):
        triangle2.forward(120)
        triangle2.left(120)
        yval += 13    
        
triangle2.end_fill()
triangle2.up()


#circle 1 that is a flower 
circle = turtle.Turtle()
circle.speed(10)
circle.up()
circleColors = ("VioletRed","VioletRed1","VioletRed2")
#colors are random because flowers change colors 

circle.goto(0,-50)
circle.color(random.choice(circleColors))
circle.begin_fill()

circle.down()

#this loop creates first flower 
xval = 0

for i in range(12):
    circle.goto(xval,-50)
    circle.left(150)
    circle.circle(50)
    xval+= 7 
    
circle.end_fill()
circle.up()

#circle 2 that is a flower 
circle2= turtle.Turtle()
circle2.up()
circle2.color("yellow")

circle2.goto(100,120)
circle2.down()
circle2.begin_fill()

#this loop creates second flower 
xval = 100

for i in range(12):
    circle2.goto(xval,120)
    circle2.left(100)
    circle2.circle(25)
    xval+= 10   
    
circle2.end_fill()

#circle 3 that is a flower 
circle3= turtle.Turtle()
circle3.up()
circle3.color("orange")

circle3.goto(-80,-200)
circle3.down()
circle3.begin_fill()

#this loop creates 3rd flower
xval = -70

for i in range(12):
    circle3.goto(xval,-200)
    circle3.left(200)
    circle3.circle(35)
    xval+= 15   
    
circle3.end_fill()

    



    
    
    
         










# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
