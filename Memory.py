"""Memory, a puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tiles.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from freegames import path

# Load the car image
car = path('car.gif')

# Create a list of number pairs for the tiles
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Initialize the tap count

# Function to draw a white square with a black outline at (x, y)
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Function to convert (x, y) coordinates to a tile index
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Function to convert a tile count to (x, y) coordinates
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Function to check if all tiles have been revealed
def all_tiles_revealed():
    return all(not tile_hidden for tile_hidden in hide)

# Function to handle tile taps and update the game state
def tap(x, y):
    global tap_count  # Declare tap_count as a global variable

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    tap_count += 1  # Increment the tap count

# Function to draw the game board
def draw():
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
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display the tap count on the screen
    up()
    goto(-180, -180)  # Adjust the position as needed
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

    if all_tiles_revealed():
        up()
        goto(0, 0)  # Adjust the position for the message
        color('green')  # You can choose the color you prefer
        write('Congratulations! You uncovered all tiles!', align='center', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

# Shuffle the tiles to randomize their positions
shuffle(tiles)

# Set up the turtle window
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)

# Register the tap function to handle mouse clicks
onscreenclick(tap)

# Start the game loop by calling the draw function
draw()

# Finish the game
done()
