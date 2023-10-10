from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.goto(0, 270)
        self.points = 0
        self.display_score()

    def display_score(self):
        self.write(f'Score: {self.points}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.points += 1
        self.clear()
        self.display_score()
