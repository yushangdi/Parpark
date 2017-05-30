# constants.py
# Shangdi Yu(sy543)
# 27/11/2016
"""Constants for Breakout

This module global constants for the game Breakout.  These constants 
need to be used in the model, the view, and the controller. As these
are spread across multiple modules, we separate the constants into
their own module. This allows all modules to access them."""
import colormodel
import sys


######### WINDOW CONSTANTS (all coordinates are in pixels) #########

#: the width of the game display 
GAME_WIDTH  = 660
#: the height of the game display
GAME_HEIGHT = 960


######### PADDLE CONSTANTS #########

#: the width of the paddle
PADDLE_WIDTH  = 58
#: the height of the paddle
PADDLE_HEIGHT = 11
#: the distance of the (bottom of the) paddle from the bottom
PADDLE_OFFSET = 30


######### BRICK CONSTANTS #########

#: the horizontal separation between bricks
BRICK_SEP_H    = 5
#: the vertical separation between bricks
BRICK_SEP_V    = 4
#: the height of a brick
BRICK_HEIGHT   = 120
#: the offset of the top brick row from the top
BRICK_Y_OFFSET = 60
BRICK_X_OFFSET = 60
#: the number of bricks per row
BRICKS_IN_ROW  = 9
#: the number of rows of bricks, in range 1..10.
BRICK_ROWS     = 2
#: the width of a brick
BRICK_WIDTH    = 60


######### BALL CONSTANTS #########

#: the diameter of the ball in pixels
BALL_DIAMETER = 20


######### GAME CONSTANTS #########

#: the number of attempts in a game
NUMBER_TURNS = 3
#: state before the game has started
STATE_INACTIVE  = 0
#: state when we are initializing a new game
STATE_NEWGAME   = 1
#: state when we are counting down to the ball serve
STATE_COUNTDOWN = 2
#: state when we are waiting for user to click the mouse
STATE_PAUSED    = 3
#: state when the ball is in play and being animated
STATE_ACTIVE    = 4


######### COMMAND LINE ARGUMENTS TO CHANGE NUMBER OF BRICKS IN ROW #########
"""sys.argv is a list of the command line arguments when you run
python. These arguments are everything after the work python. So
if you start the game typing

    python breakout.py 3 4
    
Python puts ['breakout.py', '3', '4'] into sys.argv. Below, we 
take advantage of this fact to change the constants BRICKS_IN_ROW
and BRICK_ROWS"""

try:
   if (not sys.argv is None and len(sys.argv) == 3):
        bs_in_row  = int(sys.argv[1])
        brick_rows = int(sys.argv[2])
        if (bs_in_row > 0 and brick_rows > 0):
            # ALTER THE CONSTANTS
            BRICKS_IN_ROW  = bs_in_row
            BRICK_ROWS     = brick_rows
            BRICK_WIDTH    = GAME_WIDTH / BRICKS_IN_ROW - BRICK_SEP_H
except: # Leave the contants alone
    pass


######### ADD MORE CONSTANTS (PROPERLY COMMENTED) AS NECESSARY #########
#: the number of total states
NUM_STATES  = 5
#: the list of possible brick colors in order 
BRICK_COLORS = [colormodel.RED, colormodel.ORANGE, colormodel.YELLOW,
                colormodel.GREEN, colormodel.CYAN]
#: state when the game has ended
STATE_COMPLETE = 5
