"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import turtle
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
    turtle.pencolor("blue")  # Change to blue color
    turtle.width(5)  # Change thickness
    line(x + 23, y + 23, x + 110, y + 110)  # Draw a diagonal
    line(x + 23, y + 110, x + 110, y + 23)  # Draw a back slash diagonal
    # Both lines should measure the size of the square, 133 pixels


def drawo(x, y):
    """Draw O player."""
    """x and y are coordinates"""
    turtle.pencolor("red")  # Change to red color
    turtle.width(5)  # Change thickness
    size = 133  # Square size for x
    radius = 50  # Circle radius
    turtle.up()  # Use up() to move the cursor without drawing lines

    # Use goto() to center point of the O
    turtle.goto(x + size / 2, y + radius / 3)
    turtle.setheading(0)  # Point the turtle to the right
    turtle.down()  # Use down() to draw lines when movement occur

    # Use circle() to draw a circle with a radius of () pixels
    turtle.circle(radius)


def floor(value):
    """Round value down to grid with square size 133."""
    """Place X and O centers on square's centers"""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}  # Changes between 0 and 1
players = [drawx, drawo]  # A list that draws the correct symbol each turn


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)  # Draw x coordinate on square's center
    y = floor(y)  # Draw y coordinate on square's center
    player = state['player']  # Obtain the value 0(X) or 1(O)
    draw = players[player]  # Draw X or O depending on the turn

    # Call is_occupied() and compare
    if is_occupied(x, y):
        return  # Exit def tap without doing anything
    # Turn will change only if player selects an unoccupied square

    draw(x, y)  # Draw X or O where clicked calling drawx and drawo
    turtle.update()  # Updates output screen
    state['player'] = not player  # Change turn

    # Add new occupied square to the list of occupied positions
    occupied_positions.append((x, y))


def is_occupied(x, y):
    """Check if a square is already occupied."""
    # Iterate over the occupied positions and check if it maches (x, y)
    for x_occupied, y_occupied in occupied_positions:
        if x == x_occupied and y == y_occupied:
            return True  # The square is occupied
    return False  # The square is not occupied


occupied_positions = []  # This list keeps track of occupied positions


turtle.setup(420, 420, 370, 0)  # Screen size
turtle.hideturtle()  # For turtle graphics
turtle.tracer(False)  # Updates will be fluid
grid()  # Calls def grid
turtle.update()  # Calls def update
turtle.onscreenclick(tap)  # Click function
turtle.done()  # End program
