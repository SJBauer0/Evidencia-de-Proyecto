"""Memorama, el juego de rompecabezas de pares de números.

Ejercicios:
1. Cuenta e imprime el número de toques.
2. Decrece el número de fichas a una cuadícula de 4x4.
3. Detecta cuando todas las fichas sean reveladas.
4. Centraliza fichas con números de un dígito.
5. Usa letras en vez de números.

"""

from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward, left
from turtle import end_fill, clear, shape, stamp, write, update
from turtle import ontimer, setup, addshape, hideturtle, tracer
from turtle import onscreenclick, done
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Dibuja un cuadro blanco con margen negro en (x,y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x,y) en índice de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte la cuenta de fichas a coordenadas (x,y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza la marca y las fichas ocultas basándose en los toques."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja la imagen y las fichas."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    if hide == [False] * 64:
        print("Todos los mosaicos han sido revelados")

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+17, y+10)
        color('black')
        write(tiles[mark], font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
