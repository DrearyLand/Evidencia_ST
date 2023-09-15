"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    """Draw the lines to create 9 squares"""
    line(-67, 200, -67, -200)  # left vertical line
    line(67, 200, 67, -200)  # right vertical line
    line(-200, -67, 200, -67)  # bottom horizontal line
    line(-200, 67, 200, 67)  # top horizontal line


def drawx(x, y):
    """Draw X player."""
    """x and y are coordinates"""
    line(x, y, x + 133, y + 133)  # Draw a back slash diagonal
    line(x, y + 133, x + 133, y)  # Draw a diagonal


def drawo(x, y):
    """Draw O player."""
    """x and y are coordinates"""
    up()  # Use up() to move the cursor without drawing lines
    goto(x + 67, y + 5)  # Use goto(), the center point of the O
    down()  # Draw lines when movement occur
    circle(62)  # Use circle() to draw a circle with a radius of () pixels


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()