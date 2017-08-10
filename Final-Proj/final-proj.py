import turtle

turtle.bgpic('bg.gif')

turtle.penup()


turtle.goto(0,-118)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction= UP
def left():
    global direction
    direction=LEFT
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.shape('ln.gif')
    turtle.goto(x-30,y)
   

    
    #print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.shape('rn.gif')
    turtle.goto(x+30,y)
    
    #print(turtle.pos())

LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'

turtle.onkeypress(left, LEFT_ARROW)

turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

turtle.register_shape('rn.gif')
turtle.register_shape('ln.gif')

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
