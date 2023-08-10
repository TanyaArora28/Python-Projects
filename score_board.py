from turtle import Turtle
FONT = ("Courier",  24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.color("coral")
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level : {self.current_level}", align="left", font=FONT)

    def increment_level(self):
        self.current_level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.color("blue")
        self.write("GAME OVER !", align="center", font=FONT)
