from random import *
from turtle import *

from freegames import path

car = path('car.gif')
keyboard_chars = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
                  '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?',
                  ' ', '\t', '\n',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Asegurate de que la lista de caracteres tenga suficientes elementos para llenar los tiles
assert len(keyboard_chars) >= 32, "La lista de caracteres debe tener al menos 32 elementos."
tiles = keyboard_chars[:32] * 2
state = {'mark': None, 'counter': 0}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
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
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    state['counter'] += 1  # Actualiza el contador de toques


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x +         2, y)
        color('black')
        # Cambiamos el tipo de fuente a monoespaciada para que todos los caracteres tengan el mismo ancho
        write(tiles[mark], font=('Courier', 30, 'normal'))

    # Muestra el contador en la pantalla
    up()
    goto(-180, 180)  # Posición fija de la pantalla
    color('black')
    write(f'Touches: {state["counter"]}', font=('Arial', 16, 'normal'))

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
,,.