#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thais
#
# Created:     24/10/2018
# Copyright:   (c) thais 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
def draw_bar(t,height):
     "Get turtle t to draw one bar, of height"
     t.begin_fill()
     t.left(90)
     t.forward(height)
     t.write("  "+str(height))
     t.right(90)
     t.forward(40)
     t.right(90)
     t.forward(height)
     t.left(90)
     t.end_fill()
     t.forward(10)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.color("blue","red")
tess.pensize(3)

xs=[48,117,200,240,160,260,220]

for a in xs:
     draw_bar(tess,a)

wn.mainloop()

#Histograma
import turtle
def draw_bar(t,height):
     "Get turtle t to draw one bar, of height"
     t.begin_fill()
     t.left(90)
     t.forward(height)
     t.write("  "+str(height))
     t.right(90)
     t.forward(40)
     t.right(90)
     t.forward(height)
     t.left(90)
     t.end_fill()

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.color("blue","red")
tess.pensize(3)

xs=input('Digite os valores de frequência')

for a in xs:
     draw_bar(tess,a)

wn.mainloop()