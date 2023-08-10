from turtle import Turtle

TURTLE_STARTING_POSITION = (0, -280)
DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("red")
        self.penup()
        self.go_to_start()

    def move(self):
        self.forward(DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(TURTLE_STARTING_POSITION)

