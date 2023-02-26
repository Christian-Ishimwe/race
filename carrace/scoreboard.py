from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        
        super().__init__()
        with open("scope.txt") as file:
            more=int(file.read())
        self.high_score=more
        self.final_score=0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280,280)
        self.write(f"Score : {self.final_score}  highscore:{self.high_score}")

        
    def call(self):
        self.final_score+=1
        self.clear()
        self.goto(-280,280)
        self.write(f"Score : {self.final_score}  highscore: {self.high_score}",40)
    def end(self):
        self.goto(0,0)
        self.write(f"Game over! \n Score: {self.final_score}")
    def reset(self):
        
        if self.high_score<self.final_score:
            self.high_score=self.final_score
            
        self.final_score=0
        # self.call()
    def overall(self):
        self.higher=self.high_score
        return self.higher