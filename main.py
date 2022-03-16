import turtle
from turtle import Turtle, Screen
import random

has_race_started = False

screen = Screen()
sprite_width = 30
sprite_height = 20 # size of sprite is 20px
turtle_center = sprite_height / 2
WIDTH = 640
HEIGHT = 480
SCREEN_TOP = HEIGHT / 2
SCREEN_BOTTOM = -SCREEN_TOP
SCREEN_RIGHT = WIDTH / 2
SCREEN_LEFT = -SCREEN_RIGHT
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def instantiate_turtles():
    num_turtles = len(turtle_colors)
    padding = 50
    start_y_pos = (SCREEN_BOTTOM / num_turtles) - (padding + sprite_height)   #somewhat center out the turtles
    for color in turtle_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()

        new_turtle.color(color)
        new_turtle.goto(SCREEN_LEFT + sprite_width, start_y_pos)
        start_y_pos += padding
        turtles.append(new_turtle)

screen.setup(width=WIDTH, height=HEIGHT)
instantiate_turtles()

player_pick = screen.textinput(title="Pick A Turtle", prompt="Enter which colored turtle will win. ")
is_valid_turtle = False
while not is_valid_turtle:
    if player_pick.lower() in turtle_colors:
        is_valid_turtle = True
    else:
        player_pick = screen.textinput(title="Choose again", prompt="Enter a valid color for your pick. ")



has_race_started = True
winner = ""
while has_race_started:

    for t in turtles:
        if t.xcor() >= SCREEN_RIGHT - sprite_width:
            has_race_started = False
            winner = t.color()
            break
        else:
            random_move_count = random.randint(0, 10)
            t.fd(random_move_count)

format_winner = winner[0]
if player_pick == format_winner:
    print("YOU WIN!!!")
else:
    print(f"Sorry the {format_winner} turtle won.")
screen.exitonclick()
