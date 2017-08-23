import turtle
import random
turtle.register_shape('fireball.gif')
turtle.register_shape('sc.gif')
turtle.register_shape('pizza.gif')

character=turtle.clone()
character.shape('sc.gif')
height = 600
character.penup()
character.goto(0,-height/2+100)

width = 800
unitsize = 20
turtle.tracer(1,0)
turtle.setup(width,height)
#turtle.hideturtle()
turtle.penup()
counter_fireballs=0

fire_list = []
step = 20
bottom = -height/2 + 100

def create_fire():
    y_pos = height/2 - 40
    min_x = -int(width/2/unitsize)+1
    max_x = int(width/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    fire = turtle.clone()
    fire.shape('fireball.gif')
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
            a=25	
            b=40
            cx=character.pos()[0]
            cy=character.pos()[1]
            y_pos = y_pos - step
            fire.goto(x_pos,y_pos)
            if(x_pos>=cx-a)and(x_pos<=cx+a)and(y_pos>=cy-b)and(y_pos<=cy+b):
                ind = fire_list.index(fire)
                fire_destroy.append(ind)
                lose_heart()
                fire.ht()
                fire.goto(1000,1000)

        else:
            ind = fire_list.index(fire)
            fire_destroy.append(ind)


    for ind in fire_destroy:
        old_fire = fire_list.pop(ind)
        old_fire.hideturtle()
        del old_fire
    if counter_fireballs == 4:
        create_fire()
        counter_fireballs=0    
    turtle.ontimer(falling_fire,100)
create_fire()
falling_fire()
    




SIZE_X = 800
SIZE_Y = 600
turtle.setup(SIZE_X,SIZE_Y)
##################################################################
width = 800
height = 600
unitsize = 20
turtle.tracer(1,0)
turtle.setup(width,height)
turtle.hideturtle()
turtle.penup()
counter_healthfood=0
#counter_fireballs=0


food_list = []
#fire_list = []


step = 20
bottom = -height/2 + 100

def create_food():
    y_pos = height/2 - 50
    min_x = -int(width/2/unitsize)+1
    max_x = int(width/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    food = turtle.clone()
    food.shape('square')
    food.goto(x_pos,y_pos)
    food.showturtle()
    food_list.append(food)

def falling_food():
    global counter_healthfood
    counter_healthfood += 1
    food_destroy = []
    for food in food_list:
        x_pos = food.pos()[0]
        y_pos = food.pos()[1]
        if y_pos >= bottom:
            d=25	
            e=40
            cx=character.pos()[0]
            cy=character.pos()[1]
            y_pos = y_pos - step
            food.goto(x_pos,y_pos)
            if(x_pos>=cx-d)and(x_pos<=cx+d)and(y_pos>=cy-e)and(y_pos<=cy+e):
                gain_health()
                ind = food_list.index(food)
                food_destroy.append(ind)
        else:
            ind = food_list.index(food)
            food_destroy.append(ind)

    for ind in food_destroy:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
    if counter_healthfood ==30:
        create_food()
        counter_healthfood=0
    turtle.ontimer(falling_food,100)
create_food()
falling_food()
###########################################





#fireballs=turtle.clone()
#healthy_food=turtle.clone()




#char_pos = character.pos()
fireball_pos = []
healthy_food = []
new_health = []

maxhealth = 5
health = maxhealth

health_list = []
health_pos = []
d=50
a=50
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
turtle.register_shape('1.gif')
heart.shape('1.gif')
for position in heart_pos:
    heart.goto(position)
    new_heart=heart.stamp()
    heart_stamp_list.append(new_heart)


def lose_heart():
    current_health=len(heart_stamp_list)
    if current_health >1:
        old_stamp=heart_stamp_list.pop(-1)
        heart.clearstamp(old_stamp)
    else:
        print('you dead')
        quit()

def gain_health():
    current_health=len(heart_stamp_list)
    if current_health!= maxhealth:
        print(current_health)
        print(heart_pos)
        heart.goto(heart_pos[current_health])
        new_heart=heart.stamp()
        heart_stamp_list.append(new_heart)

turtle.register_shape('rn.gif')
turtle.register_shape('ln.gif')
character.shape('rn.gif')
turtle.bgpic('bg.gif')

turtle.penup()
turtle.hideturtle()
character.penup()

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
    character.shape('sc.gif')
    character.goto(x-20,y)
   

    
    #print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    character.pos()
    old_pos=character.pos()
    x=old_pos[0]
    y=old_pos[1]
    character.shape('sc.gif')
    character.goto(x+20,y)
    
    #print(turtle.pos())

LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


#if turtle.pos() in fireball_pos:
	#food_ind = fireball_pos.index(snake.pos())
 	#food.clearstamp(food_stamps[food_ind])
   	#food_pos.pop(food_ind)
	#food_stamps.pop(food_ind)
    #make_food()
    #w=snake.stamp()
    #pos_list.append(w)
    #stamp_list.append(w)

turtle.mainloop()
