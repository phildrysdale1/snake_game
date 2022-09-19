## ---- PACKAGES ---- ##
import turtle
import time
import random

## ---- VARIABLES ---- ##
delay = 0.2
all_body_parts = []

## ---- DISPLY ---- ##

# set up the screen
win = turtle.Screen()
win.title("Snake Game by Phil Drysdale")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0) # turn off screen updates for efficiency

## ---- OBJECTS ---- ##

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(100,100)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

## ---- FUNCTIONS ---- ##

# move head
def move_head():
    # set coords
    y = head.ycor()
    x = head.xcor()
    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right" 

## Create body_part
def create_body_part():
    body_part = turtle.Turtle()
    body_part.speed(0)
    body_part.shape("square")
    body_part.color("white")
    body_part.penup()
    all_body_parts.append(body_part)
    
## food eaten function
def food_eaten():
    if head.distance(food) < 20:
        global delay
        # Move the food to random location
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        if delay > 0.03:
            delay -= 0.002

        create_body_part()

## build body when food eaten
def build_body():
    # Move the body parts (in reverse order)
    for index in range(len(all_body_parts)-1, 0, -1):
        x = all_body_parts[index-1].xcor()
        y = all_body_parts[index-1].ycor()
        all_body_parts[index].goto(x,y)
    # Move first body part to where the head is
    if len(all_body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        all_body_parts[0].goto(x,y)

## check for collision with border and body
def collision_check():
    global all_body_parts
    # check for border collisions
    if head.xcor() > 290 or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -290:
        reset()

    # check for collisons with self
    for body_part in all_body_parts:
        if body_part.distance(head) < 20:
            reset()

def reset():
    # reset head
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    
    # hide body_parts
    for body_part in all_body_parts:
        body_part.goto(1000,1000)

    # clear segments list
    all_body_parts.clear()

## ---- INPUT ---- ##

# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")


## ---- GAME ---- ##

# main game loop
while True:
    win.update()

    food_eaten()

    build_body()

    move_head()

    collision_check()
    
    time.sleep(delay)

win.mainloop()