import turtle

SIZE_X = 800
SIZE_Y = 500
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

max_health = 5
health = max_health

health_list = []
health_pos = []
for i in range(max_health):
    health_pos.append((SIZE_X/2 - 50 -20 * i   , SIZE_Y/2 - 50))
health_pos.reverse()

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
##
##    
##    
##    
