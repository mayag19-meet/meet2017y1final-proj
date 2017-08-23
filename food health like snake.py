import turtle
import random
food_pos = []
food_stamps = []
SIZE_X=1400
SIZE_Y=1000
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
SQUARE_SIZE = 150
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2

def make_food():

    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x = (random.randint(min_x,max_x))*SQUARE_SIZE
    food_y = (random.randint(min_y,max_y))*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_pos.append((food_x, food_y))
    c = food.stamp()
    food_stamps.append(c)

make_food()
