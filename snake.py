# setup packages
import turtle
import time
import random

delay = 0.05

# set up the screen
win = turtle.Screen()
win.title("Snake Game by Phil Drysdale")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0) # turn off screen updates for efficiency

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(100,100)

# functions
## movement function
def movement():
    # set coords
    y = head.ycor()
    x = head.xcor()
    if head.direction == "up":
        head.sety(y + 5)
    if head.direction == "down":
        head.sety(y - 5)
    if head.direction == "left":
        head.setx(x - 5)
    if head.direction == "right":
        head.setx(x + 5)

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

## food eaten function
def food_eaten():
    if head.distance(food) < 20:
        # Move the food to random location
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# main game loop
while True:
    win.update()
    
    food_eaten()

    movement()

    time.sleep(delay)

win.mainloop()