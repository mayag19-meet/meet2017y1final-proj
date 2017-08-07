import turtle
import random

SIZE_X = 1000
SIZE_Y = 600

BALL_SIZE = 20

turtle.setup(SIZE_X, SIZE_Y)


#lists
fireball_stamp=[]
fireball_pos=[]

fireball = turtle.clone()
fireball.shape("circle")
fireball.penup()
TIME_STEP = 1
fireball.hideturtle()

def make_fireball():
    min_x=-int(SIZE_X/3/BALL_SIZE)+1
    max_x=int(SIZE_X/2/BALL_SIZE)-1

    
    fire_ballX = random.randint(min_x, max_x)*BALL_SIZE
    fireball.goto(fire_ballX, SIZE_Y/2-20)
    stamp1 = fireball.stamp()
    fireball_stamp.append(stamp1)
    fireball_pos.append((fire_ballX, 300))

make_fireball()

def move_fireball():

    for i in range (len(fireball_pos)):
        new_pos = (fireball_pos[i][0], fireball_pos[i][1]-25)
        fireball.goto(new_pos)
        fireball_pos[i]=new_pos
        fireball.clearstamp(fireball_stamp[i])
        stamp = fireball.stamp()
        fireball_stamp[i]=stamp
    make_fireball()
    turtle.ontimer(move_fireball, TIME_STEP)
   
move_fireball()

    
