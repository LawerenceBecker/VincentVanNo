import turtle
from PIL import Image

class Gogh():
    def __init__(self, x, y, colors):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.pu()
        self.turtle.setpos(x, y)
        self.colors = colors
        

    def draw_image(talent, count):

        talent.turtle.color(talent.colors[count][:3])
        talent.turtle.penup()
        talent.turtle.fd(1)
        talent.turtle.pendown()
        talent.turtle.forward(0)

    def spawn_turtle(image, width, height):
        pix_val = list(image.getdata())
        allY = height/2
        talents = []
        x = 1
        z = 0

        for newY in range(0, height):
            talents.append(Gogh(-(height/2), allY, pix_val[0+(width*z):width*x]))
            x += 1
            z += 1
            allY -= 1
        
        vert = 0
        cont = 0
        for hor in range(0, width):
            for tal in talents:
                if vert == width:
                    vert = 0
                    cont += 1
                Gogh.draw_image(tal, cont)
                vert += 1