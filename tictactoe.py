"""Tic Tac Toe"""

# imports de las librerias necesarias
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
    # funcion para crear el grid
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    # Funcion para dibujar X
    color('green')
    width(8)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    # Funcion para dibujar O
    color('pink')
    width(8)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    # Redondear el valor a 133
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
count = 0
coord = []


def tap(x, y):
    # Dibujar X o O en un casilla
    x = floor(x)
    y = floor(y)
    z = (x, y)
    # Checar si una casilla esta disponible
    if (z in coord):
        print("Elije otra casilla")
    else:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        coord.append(z)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
