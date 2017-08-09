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

fire_list = []
step = 20
bottom = -height/2 + 100

def create_fire():
    y_pos = height/2 - 50
    min_x = -int(width/2/unitsize)+1
    max_x = int(width/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    fire = turtle.clone()
    fire.shape('circle')
    fire.goto(x_pos,y_pos)
    fire.showturtle()
    fire_list.append(fire)

def falling_fire():
    global counter_fireballs
    counter_fireballs += 1
    fire_destroy = []
    for fire in fire_list:
        x_pos = fire.pos()[0]
        y_pos = fire.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            fire.goto(x_pos,y_pos)
        else:
            ind = fire_list.index(fire)
            fire_destroy.append(ind)

    for ind in fire_destroy:
        old_fire = fire_list.pop(ind)
        old_fire.hideturtle()
        del old_fire
    if counter_fireballs == 2:
        create_fire()
        counter_fireballs=0
    turtle.ontimer(falling_fire,100)
create_fire()
falling_fire()
    


