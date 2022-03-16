# TODAY IS MY BIRTHDAY!!!
import turtle


my_turtle = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    my_turtle.fd(10)


def move_down():
    my_turtle.bk(10)


def reset_turtle():
    screen.reset()
    my_turtle.goto(0, 0)


def change_draw_speed():
    speed = int(my_turtle.speed())
    my_turtle.speed(speed + 1)


def rotate_left():
    my_turtle.rt(-10)


def rotate_right():
    my_turtle.rt(10)


def draw_spiro():
    for i in range(36):
        my_turtle.circle(100)
        my_turtle.rt(10)


screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="d", fun=move_down)
screen.onkeypress(key="c", fun=reset_turtle)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="1", fun=draw_spiro)
screen.onkeypress(key="Up", fun=change_draw_speed)
screen.exitonclick()
