import turtle
import random
width = 800
height = 600
unitsize = 20
turtle.tracer(1,0)
turtle.setup(width,height)
turtle.hideturtle()
turtle.penup()
counter_fireballs=0

food_list = []
step = 20
bottom = -height/2 + 100

def create_food():
    y_pos = height/2 - 50
    min_x = -int(width/2/unitsize)+1
    max_x = int(width/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    food = turtle.clone()
    food.shape('circle')
    food.goto(x_pos,y_pos)
    food.showturtle()
    food_list.append(food)

def falling_food():
    global counter_fireballs
    counter_fireballs += 1
    food_destroy = []
    for food in food_list:
        x_pos = food.pos()[0]
        y_pos = food.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            food.goto(x_pos,y_pos)
        else:
            ind = food_list.index(food)
            food_destroy.append(ind)

    for ind in food_destroy:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
    if counter_fireballs == 2:
        create_food()
        counter_fireballs=0
    turtle.ontimer(falling_food,100)
create_food()
falling_food()
    


