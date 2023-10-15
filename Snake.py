from tkinter import *
import random

BACKGROUND="black"
SNAKE_PARTS=3
GAME_SIZE=20
FOOD_COLOR="blue"
SNAKE_COLOR="green"
SPEED=50
GAME_WIDTH=700
GAME_HEIGHT=700

class Snake():
    def __init__(self):
        self.snakeParts=SNAKE_PARTS
        self.coordinates=[]
        self.squares=[]

        for i in range (0, SNAKE_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+GAME_SIZE, y+GAME_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food():
    def __init__(self):
        x=random.randint(0,GAME_WIDTH/GAME_SIZE-1)*GAME_SIZE
        y=random.randint(0,GAME_HEIGHT/GAME_SIZE-1)*GAME_SIZE

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+GAME_SIZE, y+GAME_SIZE, fill=FOOD_COLOR, tag="food")

def nextTurn(snake,food):
    x,y=snake.coordinates[0]

    if direction=="up":
        y-=GAME_SIZE

    if direction=="down":
        y+=GAME_SIZE

    if direction=="right":
        x+=GAME_SIZE

    if direction=="left":
        x-=GAME_SIZE

    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+GAME_SIZE, y+GAME_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global Score

        Score+=1

        label.config(text="Score:{}".format(Score))
        canvas.delete("food")
        food=Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if checkCollision(snake):
        gameOver()

    else:
        window.after(SPEED, nextTurn, snake, food)


def changeDirection(newDirection):
    global direction

    if newDirection=="up":
        if direction!="down":
            direction=newDirection

    if newDirection=="down":
        if direction!="up":
            direction=newDirection

    if newDirection=="left":
        if direction!="right":
            direction=newDirection

    if newDirection=="right":
        if direction!="left":
            direction=newDirection

def checkCollision(snake):
    x,y=snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        print("game over")
        return True

    if y<0 or y>=GAME_HEIGHT:
        print("game over")
        return True

    for bodyparts in snake.coordinates[1:]:
        if x==bodyparts[0]and y==bodyparts[1]:
            print("game over")
            return True

    return False

def gameOver():
    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       tag="game over", font=("impact", 50), text="Game Over", fill="red")

window=Tk()
window.title("Snake Game")
window.resizable(False,False)

direction="down"
Score=0

label=Label(window, text="Score:{}".format(Score), font=("impact",30))
label.pack()

canvas=Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH, bg=BACKGROUND)
canvas.pack()

window.update()

windowWidth=window.winfo_width()
windowHeight=window.winfo_height()
screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_height()

x=int((screenWidth/2)-(windowWidth/2))
y=int((screenHeight/2)-(windowHeight/2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

window.bind("<Right>", lambda event: changeDirection("right"))
window.bind("<Left>", lambda event: changeDirection("left"))
window.bind("<Up>", lambda event: changeDirection("up"))
window.bind("<Down>", lambda event: changeDirection("down"))

food=Food()
snake=Snake()
nextTurn(snake, food)

window.mainloop()