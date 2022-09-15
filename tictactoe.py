"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
"""
from turtle import up
from turtle import done
from turtle import goto
from turtle import circle
from turtle import down
from turtle import update
from turtle import onscreenclick
from turtle import tracer
from turtle import hideturtle
from turtle import setup
from turtle import color
from turtle import width
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('green')
    width(8)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw O player."""
    color('pink')
    width(8)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
count = 0
coord = []


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    z = (x, y)
    if (z in coord):
        print("Elije otra casilla")
    else:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        coord.append(z)


def counter():
    global count
    count += 1
    return count


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
