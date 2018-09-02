"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Bert.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
jacky = rg.SimpleTurtle('arrow')
blue_turtle = rg.SimpleTurtle('turtle')
jacky.pen = rg.Pen('red',30)
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 5  # Fast
# The first square will be 300 x 300 pixels:
size1 = 50
blue_turtle.go_to(rg.Point(-100, 0))
jacky.pen_up()
# Do the indented code 13 times.  Each time draws a square.

for k in range(13):

    # Put the pen down, then draw a square of the given size:
    jacky.pen_down()
    blue_turtle.draw_circle(size1)
    blue_turtle.go_to(rg.Point(100,0))
    blue_turtle.draw_circle(size1)
    blue_turtle.go_to(rg.Point(-75,0))
    blue_turtle.go_to(rg.Point(-75,200))
    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    jacky.draw_square(50)
    jacky.pen_up()
    jacky.right(45)
    jacky.forward(20)
    jacky.left(45)
    jacky.pen_down()
    size1 = size1 - 2