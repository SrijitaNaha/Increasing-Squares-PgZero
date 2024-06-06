import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300


def draw():
    r = 0
    g = 0
    b = randint(120, 255)

    width = WIDTH
    height = HEIGHT - 200

    for i in range(10):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))
        
        r += 5

       
        width -= 10
        height += 10


pgzrun.go()