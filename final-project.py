import turtle
import random

turtle.tracer(1,0)

turtle.bgcolor('black')
square=turtle.clone()
square.shape('square')
square.pensize(10)
square.pencolor('red')
square.penup()
square.goto(-400,-250)
square.pendown()
square.goto(-400,250)
square.goto(400,250)
square.goto(400,-250)
square.goto(-400,-250)
square.hideturtle()

score=turtle.clone()
score.goto(250,400 )
score.color('red')


SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X+50, SIZE_Y+50)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1
SCORE = 0


UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
DOWN_ARROW = 'Down'
RIGHT_ARROW = 'Right'
TIME_STEP = 100

SPACEBAR = 'space'

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.register_shape("basketball.gif")
snake = turtle.clone()
snake.shape("basketball.gif")



turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos += SQUARE_SIZE
    my_pos = (x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    sstamp = snake.stamp()
    stamp_list.append(sstamp)

def make_food():
    min_x = -int(SIZE_X/2/SQUARE_SIZE)+1
    max_x = int(SIZE_X/2/SQUARE_SIZE)-1
    min_y = -int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y = int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = random.randint(min_x,max_x) *SQUARE_SIZE
    food_y = random.randint(min_y,max_y) *SQUARE_SIZE
    food.goto(food_x,food_y)
    k = (food_x,food_y)
    food_pos.append(k)
    xfoodx = food.stamp()
    food_stamps.append(xfoodx)
    

direction = UP
UP_EDGE = 250
def up():
    global direction
    if direction != DOWN:
        direction = UP
        #move_snake()
        print('You pressed the up key!')
    
DOWN_EDGE = -250
def down():
    global direction
    if direction != UP:
        direction = DOWN
        #move_snake()
        print('You pressed the down key!')

LEFT_EDGE = -400
def left():
    global direction
    if direction != RIGHT:
        direction = LEFT
        #move_snake()
        print('You pressed the left key!')

RIGHT_EDGE = 400
def right():
    global direction
    if direction != LEFT:
        direction = RIGHT
        #move_snake()
        print('You pressed the right key!')

def printScore():
    turtle.color("lightblue")
    turtle.goto(-(SIZE_X / 2) + 10, (SIZE_Y / 2) - 30)
    turtle.clear()
    turtle.write("Score: " + str(SCORE), False, "left", ("Arial", 16, "normal"))
    turtle.ontimer(printScore, 1000)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]


    
    
 
    global food_stamps, food_pos, SCORE
    
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        make_food()
        w=snake.stamp()
        pos_list.append(w)
        stamp_list.append(w)
        
        SCORE += 1

    if new_y_pos >= UP_EDGE:
        print("you hit the upper edge... game over")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you hit the right lower... game over")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you hit the left edge... game over")
        quit()

    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge... game over")
        quit()


        
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right!')
    
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('you moved left!')
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('you moved down!')
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print('you moved up!')

    if snake.pos() in pos_list[0:-1]:
        quit()
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    turtle.ontimer(move_snake,TIME_STEP)

printScore()
move_snake()


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

turtle.register_shape("hoop.gif")
food = turtle.clone()
food.shape("hoop.gif")

make_food()
##food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
##food_stamps = []
##for a in food_pos:
##    food.goto(a)
##    food_stamp = food.stamp()
##    food_stamps.append(food_stamp)
turtle.mainloop()