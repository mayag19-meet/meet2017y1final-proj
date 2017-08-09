import turtle

SIZE_X = 800
SIZE_Y = 600
turtle.setup(SIZE_X,SIZE_Y)



character=turtle.clone()
fireballs=turtle.clone()
healthy_food=turtle.clone()
health_bar=turtle.clone()
health_bar.shape('square')


char_pos = character.pos()
fireball_pos = []
healthy_food = []
new_health = []

maxhealth = 5
health = maxhealth

health_list = []
health_pos = []
d=50
a=30
health1=(800/2 -d,600/2 -d)
health2=(800/2 -d-a,600/2 -d)
health3=(800/2 -d-a*2,600/2 -d)
health4=(800/2 -d-a*3,600/2 -d)
health5=(800/2 -d-a*4,600/2 -d)

heart=turtle.clone()
heart.hideturtle()
heart_pos=[(health1),(health2),(health3),(health4),(health5)]
heart_stamp_list=[]

heart.penup() 

for position in heart_pos:
    heart.goto(position)
    new_heart=heart.stamp()
    heart_stamp_list.append(new_heart)


def lose_heart():
    current_health=len(heart_stamp_list)
    if current_health >=1:
        old_stamp=heart_stamp_list.pop(-1)
        heart.clearstamp(old_stamp)
    else:
        print('you dead')
        quit()

def gain_health():
    current_health=len(heart_stamp_list)
    if current_health!= maxhealth:
        health.goto(health_pos[current_health])
        new_heart=heart.stamp()
        heart_stamp_list.append(new_heart)



    
#health_pos.reverse()

##for health in health_pos:
##
##if fireball_pos in stick.pos:
##    health_bar = health_bar -1
##
##if stick.pos in healthy_food.pos:
##    if health = max_health:
##        health = 5
##    else:
##        new_health = health + 1
