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
fireball.penup()
TIME_STEP = 150

def make_fire_ball():
    min_x=-int(SIZE_X/3/BALL_SIZE)+1
    max_x=int(SIZE_X/2/BALL_SIZE)-1

    
    fire_ballX = random.randint(min_x, max_x)*BALL_SIZE
    fireball.goto(fire_ballX, SIZE_Y/2-20)
    stamp1 = fireball.stamp()
    fireball_stamp.append(stamp1)
    fireball_pos.append((fire_ballX, 300))



##def move_fire_ball():
##    fireball.goto(randx, 450)
##    fireball.ontimer(move_fireball, TIME_STEP)
##    for ball in fireball_pos:
##        ball[1] - 50
    
