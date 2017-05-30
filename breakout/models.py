# models.py
# Shangdi Yu(sy543)
# 27/11/2016
# Some of my methods referenced the CS1110 lectures.# models.py

"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.

class Car(GEllipse):
    """An instance is a parked car.
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getX(self):
        """Returns: The x attribute of this paddle.
        """
        return self.x
    
    def getY(self):
        """Returns: The y attribute of this paddle.
        """
        return self.y
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self,x,y,r):
        """Initializer: Creates a new paddle with the given bottom center point,
           width, height, and color.
        
        Parameter x: initial x coordinate of the center of the paddle
        Precondition: x is an int or float
        
        Parameter y: initial y coordinate of the bottom of the paddle
        Precondition: x is an int or float
        
        Parameter w: width of the paddle
        Precondition: w is an int or float > 0
        
        Parameter h: height of the paddle
        Precondition: h is an int or float > 0
        
        Parameter c: color of the paddle
        Precondition: c is a valid color value
        """
        GEllipse.__init__(self, x=x,y=y,width=r,height=r,fillcolor=colormodel.BLACK)
        
        
class Paddle(GEllipse):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getX(self):
        """Returns: The x attribute of this paddle.
        """
        return self.x
    
    def getY(self):
        """Returns: The y attribute of this paddle.
        """
        return self.y
    
    # INITIALIZER TO CREATE A NEW PADDLE
    def __init__(self,x,y,r,c):
        """Initializer: Creates a new paddle with the given bottom center point,
           width, height, and color.
        
        Parameter x: initial x coordinate of the center of the paddle
        Precondition: x is an int or float
        
        Parameter y: initial y coordinate of the bottom of the paddle
        Precondition: x is an int or float
        
        Parameter w: width of the paddle
        Precondition: w is an int or float > 0
        
        Parameter h: height of the paddle
        Precondition: h is an int or float > 0
        
        Parameter c: color of the paddle
        Precondition: c is a valid color value
        """
        GEllipse.__init__(self, x=x,y=y,width=2*r,height=2*r,fillcolor=c)
        
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS     
    def moveR(self):
        """Move this paddle 3 pixiels to the right when called
        """
        self.x = self.x+3
    
    def moveL(self):
        """Move this paddle 3 pixiels to the left when called
        """
        self.x = self.x-3
    
    def moveU(self):
        self.y=self.y+3
        
    def moveD(self):
        self.y = self.y -3
        
    def collides(self,ball):
        """Returns: 'left' if the ball collides with this paddle's left half
                    'right' if the ball collides with this paddle's middle
                             or right half
                    'False' if no collision happens
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball
        """
        bottom= self.contains(ball.getX(), ball.getBottom())
        left = self.contains(ball.getLeft(), ball.getY())
        right = self.contains(ball.getRight(), ball.getY())
        
        if bottom or left or right:
            if ball.getX()<self.x:
                return "left"
            return 'right'
        else:
            return 'False'
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Arrow(GEllipse):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self,x,y,w,h,n):
  
        GEllipse.__init__(self,x=x,y=y,width=w,height=h,
                            fillcolor=colormodel.GREEN, linecolor=colormodel.BLUE)
        self._emptylist=n
        
    def changecolor(self):

        self.fillcolor=colormodel.RED
    
    def park(self):
        self._emptylist= self._emptylist-1
        if self._emptylist<=0:
            self.changecolor(False)
        

class Brick(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self,x,y,w,h,c1,c2):

        GRectangle.__init__(self,x=x,y=y,width=w,height=h,
                            fillcolor=c1,linecolor=c2)
        
    # METHOD TO CHECK FOR COLLISION
    def collides(self,paddle):
        """Returns: True if the ball collides with this brick
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball
        """
        bottom= self.contains(paddle.getX(), paddle.getY())
        #top= self.contains(ball.getX(), ball.getTop())
        #left = self.contains(ball.getLeft(), ball.getY())
        #right = self.contains(ball.getRight(), ball.getY())
        return bottom


    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

class Sign(GImage):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO CREATE A BRICK
    def __init__(self,x,y,w,h,s):

        GImage.__init__(self, x=x,y=y,width=w,height=h,source=s)
        
class Ball(GImage):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getBottom(self):
        """Returns: The y coordinate of the bottom of this ball.
        """
        return self.bottom
    
    def getTop(self):
        """Returns: The y coordinate of the top of this ball.
        """
        return self.top
    
    def getLeft(self):
        """Returns: The x coordinate of the left of this ball.
        """
        return self.left
    
    def getRight(self):
        """Returns: The x coordinate of the right of this ball.
        """
        return self.right
    
    def getX(self):
        """Returns: The x coordinate of the center of this ball.
        """
        return self.x
    
    def getY(self):
        """Returns: The y coordinate of the center of this ball.
        """
        return self.y

    
    # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self,x,y):
        """Initializer: Creates a new ball with width=BALL_DIAMETER,
                        height=BALL_DIAMETER, _vy=-0.2, a random _vx between
                        -5.0 to -1.0 or 1.0 to 5.0, 
                        source='beach-ball.png', and the given center position.
        If _vx is positive, the ball moves to the right, if _vx is negative,
        the ball moves to the left.
        If _vy is positive, the ball moves up, if _vy is negative, the ball
        moves down.
        
        Parameter x: initial x coordinate of the center of the ball
        Precondition: x is an int or float
        
        Parameter y: initial y coordinate of the center of the ball
        Precondition: x is an int or float
        """
        GImage.__init__(self,x=x,y=y,
                        width=BALL_DIAMETER ,height=BALL_DIAMETER,
                        source='beach-ball.png')
        self._vx = random.uniform(1.0,5.0)
        self._vx = self._vx * random.choice([-1, 1])
        self._vy=-2.0
        
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    def negate_vy(self):
        """Make the _vy attribute negative so that the ball moves in the
        opposite direction vertically
        """
        self._vy=-self._vy
        
    def negate_vy_help(self):
        """Make the y attribute of the top of the ball equal to the top
        of the game display
        """
        self.top = GAME_HEIGHT
        
    def negate_vy_help_paddle(self):
        """Make the y attribute of the bottom of the ball equal to the top
        of the paddle
        """
        self.bottom = PADDLE_OFFSET+PADDLE_HEIGHT
        
    def negate_vx(self):
        """Make the _vx attribute negative so that the ball moves in the
        opposite direction hotizontally
        """
        self._vx=-self._vx
        
    def negate_vx_help_left(self):
        """Make the x attribute of the left of the ball equal to the left
        of the game display
        """
        self.left = 0
        
    def negate_vx_help_right(self):
        """Make the x attribute of the right of the ball equal to the right
        of the game display
        """
        self.right = GAME_WIDTH
        
    def move(self):
        """Move the ball at the velocity of _vx horizontally and _vy vertically
           
           This ball moves _vx horizontally and _vy vertically when this method
           is called once
        """
        self.x=self.x+self._vx
        self.y=self.y+self._vy
        
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE