import turtle as t
import random


tim = t.Turtle()

colors = ['CornflowerBlue','DarkOrchid','DeepSkyBlue', 'IndianRed']

########### Challenge 3 - Draw Shapes ########
def draw_shape(num_sides):
  angle = 360/num_sides
  for i in range(num_sides):
     tim.forward(100)
     tim.right(angle)

for shape in range(3,11):
  tim.color(random.choice(colors))
  draw_shape(shape)
