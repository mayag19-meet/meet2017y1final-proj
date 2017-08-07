import turtle

turtle.register_shape('5.gif')
turtle.register_shape('4.gif')
turtle.register_shape('3.gif')
turtle.register_shape('2.gif')
turtle.register_shape('1.gif')
turtle.bgpic('ted.gif')

turtle.penup()

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction= UP
def left():
    global direction
    direction=LEFT
    turtle.shape('ln.gif')
    #print('you pressed left')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-5,y)
    #print(turtle.pos())
def right():
    global direction
    direction=RIGHT
    turtle.shape('rn.gif')
    #print('you pressed right')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+5,y)
    #print(turtle.pos())

LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'

turtle.onkeypress(left, LEFT_ARROW)

turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

turtle.register_shape("stick.gif")
turtle.register_shape('rn.gif')
turtle.register_shape('ln.gif')
turtle.shape('stick.gif')

turtle.mainloop()