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
 ############################

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
a=45
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
    #heart.shape('1.gif')
    new_heart=heart.stamp()
    heart_stamp_list.append(new_heart)
##################################
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

#######################

##turtle.register_shape('ln.gif')
##turtle.register_shape('rn.gif')
##turtle.register_shape('5.gif')
##turtle.register_shape('r3.gif')
##turtle.register_shape('r4.gif')
##turtle.register_shape('r5.gif')
##turtle.register_shape('l1.gif')
##turtle.register_shape('l2.gif')
##turtle.register_shape('l3.gif')
##turtle.register_shape('l4.gif')
##turtle.register_shape('l5.gif')
##turtle.bgpic('ted.gif')
healthbar=turtle.clone()
healthbar.penup()
healthbar.goto(150,300)
##healthbar.shape('5.gif')
##turtle.bgpic('bg.gif')



character.goto(0,-118)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction= UP
def left():
    global direction
    direction=LEFT
    old_pos=character.pos()
    x=old_pos[0]
    y=old_pos[1]
    character.shape('ln.gif')
    character.goto(x-30,y)
   

    
    #print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    character.pos()
    old_pos=character.pos()
    x=old_pos[0]
    y=old_pos[1]
    character.shape('rn.gif')
    character.goto(x+30,y)
    
    #print(turtle.pos())

LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'

character.onkeypress(left, LEFT_ARROW)

character.onkeypress(right, RIGHT_ARROW)
character.listen()

##turtle.register_shape('rn.gif')
##turtle.register_shape('ln.gif')
##
###if turtle.pos() in fireball_pos:
	#food_ind = fireball_pos.index(snake.pos())
 	#food.clearstamp(food_stamps[food_ind])
   	#food_pos.pop(food_ind)
	#food_stamps.pop(food_ind)
    #make_food()
    #w=snake.stamp()
    #pos_list.append(w)
    #stamp_list.append(w)

turtle.mainloop()


###################



def lose_heart():
    current_health=len(heart_stamp_list)
    if current_health >=1:
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



