#Mahleat Kidanemriam
#11/01/2020

#This program draws a polygon of your choice in the color of your choice
import turtle
t = turtle.Turtle()
colors=['red', 'blue', 'green', 'yellow']
def drawpo (n,l,sel,inside_col):
 t.pencolor(colors[sel])
 t.fillcolor(colors[inside_col])
 t.begin_fill() 
 for _ in range(n):
   t.forward(l)
   t.right(360 / n)
 t.end_fill()

s = int(input("Enter the number of the sides of the polygon \n"))
len = int(input("Enter the angle of the sides of the polygon \n"))
col = int(input("Enter a number corresponding to color for the line  \n0)Red\n1)Blue\n2)Green\n3)Yellow\n"))
inc= int(input("Enter a number corresponding to color to fill inside shape \n0)Red\n1)Blue\n2)Green\n3)Yellow\n"))
drawpo(s,len,col,inc)

