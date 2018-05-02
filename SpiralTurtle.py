import turtle

window=turtle.Screen()
window.bgcolor("black")


def draw_turt(xd):
    i=0
    while(i<500):
     xd.forward(i)
     xd.left(92)
     i=i+2
    
turt=turtle.Turtle()
pos=turt.position()
turt.shape("turtle")
turt.pensize(1.5)
turt.speed(0.5)


colorlist=["pink","white","magenta"]
for i in colorlist:
 turt.color(i)
 draw_turt(turt)
 turt.setpos(pos)
 turt.setheading(0)
 


