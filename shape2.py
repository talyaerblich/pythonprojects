from turtle import*
penup()
goto(0,0)
def draw_square(color):
    begin_fill()
    fillcolor(color)
    for i in range(4):
        pencolor(color)
        pendown()
        forward(80)
        right(90)
    penup()
    end_fill()
    forward(90)
    
def outline():
    pencolor("white")
    goto(-190,100)
    pendown()
    forward(280)
    right(90)
    forward(100)
    right(90)
    forward(90)
    right(270)
    forward(180)
    right(90)
    forward(100)
    right(90)
    forward(180)
    right(270)
    forward(90)
    right(90)
    forward(100)

goto(-50,-30)
dot(425,"black")
    
  


goto(-180,90)
draw_square("coral")

draw_square("gold")

draw_square("SpringGreen")

goto(-90,0)
draw_square("violet")
goto(-90,-90)
draw_square("turquoise")
outline()
penup()
