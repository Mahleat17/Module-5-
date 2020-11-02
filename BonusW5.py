#Mahleat Kidanemariam
#11/01/2020

#This program draws a tree
import turtle
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)# here we are making a recursive call right after the turtle turns to the right by 20 degrees same on line 8 but after 40 degrees to the left 
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def draw_all():
    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
draw_all()

