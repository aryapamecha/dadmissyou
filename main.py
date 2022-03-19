from turtle import Screen, Turtle
import time
import turtle


screen = Screen()
screen.bgcolor('light pink')
screen.setup(width=1920, height=1080, startx=0, starty=0)

time.sleep(2)

turtle = Turtle()
turtle.hideturtle()
turtle.color('red')
turtle.begin_fill()
turtle.fillcolor('red')
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)
turtle.setheading(60)
turtle.circle(-90, 200)
turtle.forward(180)
turtle.end_fill()
turtle.penup()

turtle.sety(-100)
turtle.color('red')
style = ('Courier', 50, 'italic')
turtle.write('I love you, Dad!', font=style, align='center')



turtle.sety(-200)
turtle.color('red')
style = ('Courier', 50, 'italic')
turtle.write( 'I miss you soo much!!', font=style, align='center')


turtle.sety(-300)
turtle.color('red')
style = ('Courier', 20, 'italic')
turtle.write('Coded by: Arya Pamecha with Python', font=style, align='center')


screen.mainloop()

