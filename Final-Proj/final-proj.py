import turtle
turtle.register_shape('r1.gif')
turtle.register_shape('r2.gif')
turtle.register_shape('5.gif')
turtle.register_shape('r3.gif')
turtle.register_shape('r4.gif')
turtle.register_shape('r5.gif')
turtle.register_shape('l1.gif')
turtle.register_shape('l2.gif')
turtle.register_shape('l3.gif')
turtle.register_shape('l4.gif')
turtle.register_shape('l5.gif')
turtle.bgpic('ted.gif')

TIME_STEP=200

healthbar=turtle.clone()
healthbar.penup()
healthbar.goto(150,300)
healthbar.shape('5.gif')

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
    turtle.shape('ln.gif')
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.shape('l1.gif')
    turtle.goto(x-4,y)
    turtle.delay(40)
    turtle.shape('l2.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-4,y)
    turtle.delay(40)
    turtle.shape('l3.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-4,y)
    turtle.delay(40)
    turtle.shape('l4.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-4,y)
    turtle.delay(40)
    turtle.shape('l5.gif')
    turtle.pos()
    old_pos=turtle.pos()
    turtle.goto(x+4,y)
    #print('you pressed right')
    turtle.pos()
    old_pos=turtle.pos()
    
    turtle.goto(x+20,y)
    #print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.shape('r1.gif')
    turtle.goto(x+4,y)
    turtle.delay(40)
    turtle.shape('r2.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+4,y)
    turtle.delay(40)
    turtle.shape('r3.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+4,y)
    turtle.delay(40)
    turtle.shape('r4.gif')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+4,y)
    turtle.delay(40)
    turtle.shape('r5.gif')
    turtle.pos()
    old_pos=turtle.pos()
    turtle.goto(x+4,y)
    #print('you pressed right')
    turtle.pos()
    old_pos=turtle.pos()
    
    turtle.goto(x+20,y)
    #print(turtle.pos())

LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'

turtle.onkeypress(left, LEFT_ARROW)

turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

turtle.register_shape('rn.gif')
turtle.register_shape('ln.gif')
turtle.mainloop()