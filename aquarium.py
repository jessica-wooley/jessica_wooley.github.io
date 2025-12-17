"""
This is a Aquarium Project that has two different types of Fish. One that is a circle fish 
and one that is a square fish. In the aquarium it has four fish total that are different 
sizes with one big circle fish, one small circle fish, one big square fish, and one small square fish.
The aquarium has decorative elements like each fish having bubbles, there being a sea plant, and a fishing sign.
"""

import turtle
# This sets the background color to blue(cyan)
s = turtle.Screen()
s.bgcolor("cyan")

#Function 1: Fish Tail
"""
This function draws the fish tail of each of the fish. Taking in the argument of 
the size of the tail, the color, and the position which makes it turn left or right.
"""
def draw_fish_tail(size,color,position):
    turtle.fillcolor(color)
    turtle.setheading(position)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


# Function 2: Circle Body
"""
This function draws the circle body of a fish. 
Taking in the argument of radius and color.
"""
def draw_circle_body(radius,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# Function 3: Square Body 
"""
This function draws the square body of a fish. 
Taking in the argument of length and color.
"""
def draw_square_body(length,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

# Function 4: Small Eyes
"""
This function draws the eyes for the fish. 
Taking in the argument of x-intercept, y-intercept, and size.
"""
def draw_black_small_eye(x,y,size):
    turtle.fillcolor("black")
    turtle.penup()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()
    return size 

# Function 5: Small Circle Body
"""
This function draws the small circle body of a fish. 
It calls the draw_circle_body function in order to make a smaller version.
"""
def draw_small_circle_body():
    draw_circle_body(45/2, "yellow")

# Function 6: Small Square Body
"""
This function draws the small square body of a fish. 
It calls the draw_square_body function in order to make a smaller version.
"""
def draw_small_square_body():
    draw_square_body(85/2, "yellowgreen")

#Function 7: Fishing Sign 
"""
This function draws the fishing sign for the aquarium.
It takes the arguments size which is the size of the sign and 
position which can turn the sign.
"""
def draw_fishing_sign(size,position):
    turtle.setheading(position)
    turtle.fillcolor("lightsalmon4")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.left(90)
    turtle.end_fill()

#Function 8: Sea Plant
"""
This function draws the sea plant for the aquarium. 
It takes the arguments x-intercept, y-intercept, and size.
"""
small_size = 50
large_size = 75

def draw_sea_plant(x,y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("green4")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.left(90)
    turtle.end_fill()

#Function 9: Bubble
"""
This function draws the bubbles for the fish. 
It takes the arguments x-intercept, y-intercept, and size.
"""
def draw_bubble(x,y,radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill() 
    turtle.circle(radius)
    turtle.end_fill()
#Function 10: Big Circle Fish

def big_circle_fish():
    turtle.penup()
    turtle.goto(-100, -10)
    turtle.pendown()
    draw_circle_body(45, "orange")
    turtle.penup()
    turtle.goto(-200, 60)
    turtle.pendown()
    draw_fish_tail(65, "red", -90)
    draw_black_small_eye(-90, 55, 8)
# Bubbles for Big Circle Fish 
    x = -50
    y= 20 
    radius = 8
    for i in range(3):
        draw_bubble(x, y, radius)
        x+= 10
        y+= 20
        radius -= 2

#Function 11: Small Circle Fish ()
def small_circle_fish():
    turtle.penup()
    turtle.goto(-32, 150)
    turtle.pendown()
    draw_small_circle_body()
    turtle.penup()
    turtle.goto(-58, 165)
    turtle.pendown()
    draw_fish_tail(30, "blue", -90)
    draw_black_small_eye(-1, 160, 4)
    
#Bubbles for Small Circle Fish
    x = 25
    y = 140
    radius = 8

    for i in range(3):
        draw_bubble(x, y, radius)
        x+= 5
        y +=20
        radius -=2

# Function 12: Big Square Fish
def big_square_fish():
    turtle.penup()
    turtle.goto(50, 10)
    turtle.pendown()
    draw_square_body(85, "Dodgerblue")
    turtle.penup()
    turtle.goto(190, -60)
    turtle.pendown()
    draw_fish_tail(65, "fuchsia", 90)
    draw_black_small_eye(80, -10, 8)
#Bubbles for Big Square Fish
    x = 40
    y = -40
    radius = 8

    for i in range(3):
        draw_bubble(x, y, radius)
        x-= 15
        y += 15
        radius -= 2
# Function 13: Small Square Fish 
def small_square_fish():
    turtle.penup()
    turtle.goto(170, 60)
    turtle.pendown()
    draw_small_square_body()
    turtle.penup()
    turtle.goto(195, 70)
    turtle.pendown()
    draw_fish_tail(30, "darkviolet", 90)
    draw_black_small_eye(140, 90, 4)
#Bubbles for Small Square Fish
    x = 110
    y= 85
    radius = 8

    for i in range(3):
        draw_bubble(x, y, radius)
        x-= 15
        y+= 15
        radius -= 2

#Function 14: Sea Plant
def sea_plant():
    x = -180
    y = -195
    for i in range (2):
        draw_sea_plant(x,y,large_size)
        x+= 25
        draw_sea_plant(x,y,small_size)
        x+=28

# Function 15: Fishing Sign
def fishing_sign():
    turtle.penup()
    turtle.goto(220, -109)
    turtle.pendown()
    draw_fishing_sign(90,-180)
    turtle.penup()
    turtle.goto(190, -205)
    turtle.pendown()
    draw_fishing_sign(50,90)

#Main Body
big_circle_fish()
small_circle_fish()
big_square_fish()
small_square_fish()
sea_plant()
fishing_sign()

turtle.done()

