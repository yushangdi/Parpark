# play.py
# Shangdi Yu(sy543)
# 27/11/2016
# Some of my methods referenced the CS1110 lectures.

"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left 
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        _score [int>= 0]: the score of the player in a game
    """
    
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getPaddle(self):
        """Returns: the paddle of this game."""
        return self._paddle
    
    def getBricks(self):
        """Returns: the list of bricks of this game."""
        return self._bricks
    
    def getBall(self):
        """Returns: the ball of this game."""
        return self._ball
    
    def getTries(self):
        """Returns: the number of tries left."""
        return self._tries
    
    def removeBall(self):
        """Removes the ball from the game
        
           It should be called when the user lost the ball.
           The _ball is set to None"""
        self._ball=None
    
    def die(self):
        """Decreases the number of tries by 1"""
        self._tries -= 1
        
    def getScore(self):
        """Returns: the score of this game."""
        return self._score
    
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer: Creates a new game with a paddle and a list of bricks.
        
        The player originally has NUMBER_TURNS of tries. There is no ball.
        The original score is 0. 
        """
        self._paddle = Paddle(30,30,BALL_DIAMETER/2,colormodel.MAGENTA)
        final_brickslist = []
        
        
        car_list=[]
        #arrow_list=[]

        list1= self.draw_helper(90, 420)
        list2=self.draw_helper(90, 120)
        list3=self.draw_helper(90, 720)
        
        final_brickslist= list1+list2+list3
        
        #arrow1=Arrow(165*2,155*2,5,5,4)
      #  arrow2=Arrow(165*2,175*2,5,5,8)
       # arrow3=Arrow(155*2,165*2,5,5,4)
        #arrow4=Arrow(175*2,165*2,5,5,8)
        
       # arrow_list.append(arrow1)
        #arrow_list.append(arrow2)
       # arrow_list.append(arrow3)
       # arrow_list.append(arrow4)
        
        default_car1=self.draw_car_helper(90, 120)
        default_car2= self.draw_car_helper(90, 420)
        default_car3=self.draw_helper(90, 720)
        default_car2[10]=None
        
        car_list=default_car1+default_car2+default_car3
        
        self._signs=self.draw_signs()
        self._bricks=final_brickslist
        self._arrows=self.initial_arrows()
        self._cars=car_list
        self._ball = None
        self._tries = NUMBER_TURNS
        self._score=0
        
    def draw_signs(self):
        signs=[]
        sign1=Sign(30,180,30,60,'up.png')
        sign2=Sign(30,480,30,60,'up.png')
        sign3=Sign(625,180,30,60,'up.png')
        sign4=Sign(625,480,30,60,'up.png')
        
        sign5=Sign(327.5,330,60,30,'right.png')
        sign6=Sign(327.5,30,60,30,'right.png')
        sign7=Sign(327.5,630,60,30,'right.png')
        
        signs.append(sign1)
        signs.append(sign2)
        signs.append(sign3)
        signs.append(sign4)
        
        signs.append(sign5)
        signs.append(sign6)
        signs.append(sign7)
        
        return signs
    
    def draw_helper(self, x,y):
        brickslist = []
        color=[[colormodel.CYAN,colormodel.BLUE],[colormodel.BLUE,colormodel.CYAN]]
        linecolor=colormodel.BLACK
        for j in range(BRICK_ROWS):
            for i in range(BRICKS_IN_ROW):  
                brick=Brick(x+BRICK_WIDTH*i,
                            y+BRICK_HEIGHT*j,
                            BRICK_WIDTH,BRICK_HEIGHT,color[i%2][j%2],linecolor)
                brickslist.append(brick)
        return brickslist
    
    def draw_car_helper(self, x,y):
        brickslist = []
        linecolor=colormodel.BLACK
        for j in range(BRICK_ROWS):
            for i in range(BRICKS_IN_ROW):  
                brick=Car(x+BRICK_WIDTH*i,
                            y+BRICK_HEIGHT*j,
                            BALL_DIAMETER )
                brickslist.append(brick)
        return brickslist
    
    def fourarrows(self, x,y,distance,r):
        arrow_list=[]
        arrow1=Arrow(x-distance,y,r,r,8)
        arrow2=Arrow(x+distance,y,r,r,8)
        arrow3=Arrow(x,y-distance,r,r,8)
        arrow4=Arrow(x,y+distance,r,r,8)
        arrow_list.append(arrow1)
        arrow_list.append(arrow2)
        arrow_list.append(arrow3)
        arrow_list.append(arrow4)
        return arrow_list
    
    def initial_arrows(self):
        list1=[]
        list1.append(self.fourarrows(15*2,15*2,10,10))
        list1[0][2]=None
        list1[0][0]=None
        list1[0][1].changecolor()
        #list1.append(self.fourarrows(165*2,15*2,10,5))
        list1.append(self.fourarrows(315*2,15*2,10,10))
        list1[1][0]=None
        list1[1][2]=None
        list1[1][1].changecolor()
        list1[1][3].changecolor()
        list1.append(self.fourarrows(15*2,165*2,10,10))
        list1[2][2]=None
        list1[2][0]=None
        list1[2][1].changecolor()
       # list1.append(self.fourarrows(165*2,165*2,10,5))
        list1.append(self.fourarrows(315*2,165*2,10,10))
        list1[3][0]=None
        list1[3][2]=None
        list1[3][1].changecolor()
        list1[3][3].changecolor()
        list1.append(self.fourarrows(15*2,315*2,10,10))
        list1[4][2]=None
        list1[4][0]=None
        list1[4][3].changecolor()
       # list1.append(self.fourarrows(165*2,315*2,10,5))
        #list1.append(self.fourarrows(315*2,315*2,10,5))
        #list1[5][0]=None
        #list1[5][2]=None
            
        return list1
        
        
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    def updatePaddle(self, i):
        """Animates the paddle.
        
        Acknowledgement: Uses code from CS1110 lectures ARROW.py
        """
        #Uses code from CS1110 lectures ARROW.py
        # Look at the key presses
        # Doing this way cause left and right to cancel each other out
        # Change the position x
        x=self._paddle.getX()


        if i.is_key_down('right'):
            self._paddle.moveR()

        if i.is_key_down('left'):
            self._paddle.moveL()
            
        if i.is_key_down('up'):
            self._paddle.moveU()
            
        if i.is_key_down('down'):
            self._paddle.moveD()
    
    def updateArrow(self, i):
        """Animates the paddle.
        
        Acknowledgement: Uses code from CS1110 lectures ARROW.py
        """
        #Uses code from CS1110 lectures ARROW.py
        # Look at the key pressess
        # Doing this way cause left and right to cancel each other out
        # Change the position x
        x=self._paddle.getX()
        y=self._paddle.getY()
        
        if self._bricks[10].collides(self._paddle):
            self._arrows[4][1].changecolor()
            self._arrows[2][3].changecolor()
            self._arrows[0][3].changecolor()


        
    def serveBall(self,x,y):
        """Creates a Ball instance and assign it to _ball."""
        self._ball= Ball(x,y)
        
    def updateBall(self):
        """Animates the ball."""
        self._ball.move()
        self.collision()
    
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def draw(self, view):
        """Draw this shape in the provide view.
        
            :param view: view to draw to
            **Precondition**: an *instance of* `GView`
        
        Ideally, the view should be the one provided by `Breakout`."""
        for i in self._bricks:
            i.draw(view)
        for j in self._arrows:
            for l in j:
                if not l is None:
                    l.draw(view)
        for car in self._cars:
            if not car is None:
                car.draw(view)
        for sign in self._signs:
            sign.draw(view)
            
        self._paddle.draw(view)
        #if not self._ball is None:
         #   self._ball.draw(view)
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def collision(self):
        """Allows the ball to collide with the frames, paddle, and bricks."""
        self._collisions_frame()     
        self._collisions_paddle()
        self._collisions_bricks()
    
    def _collisions_frame(self):
        """Helper method to allow the ball to collide with the frame."""
        if self._ball.getTop()>=GAME_HEIGHT:
            self._ball.negate_vy_help()
            self._ball.negate_vy()
            
        if self._ball.getRight()>=GAME_WIDTH:
            self._ball.negate_vx_help_right()
            self._ball.negate_vx()
            
        if self._ball.getLeft()<=0:
            self._ball.negate_vx_help_left()
            self._ball.negate_vx()        
    
    
    def _collisions_paddle(self):
        """Helper method to allow the ball to collide with the paddle.
        
         If the ball is coming down toward the right (or left) and
         hits the left (or right)
         1/2 of the paddle, the ball goes back the way it came"""
        
        if ((self._paddle.collides(self._ball) == 'right'
             and self._ball._vx>0)
            or (self._paddle.collides(self._ball) == 'left'
                and self._ball._vx<0)):
            self._ball.negate_vy_help_paddle()
            self._ball.negate_vy()
        elif self._paddle.collides(self._ball) != 'False':
            self._ball.negate_vy_help_paddle()
            self._ball.negate_vy()
            self._ball.negate_vx()
    
    def _collisions_bricks(self):
        """Helper method to allow the ball to collide with the bricks.
        
         If the ball collide with the bricks, a sound
         is played the brick is removed, the score increases and
         the ball bounces back. The score is increase more when ball.y is larger"""
        for i in self._bricks:
            if i.collides(self._ball):
                bounceSound = Sound('bounce.wav')
                bounceSound.play()
                self._bricks.remove(i)
                a= i.y-(GAME_HEIGHT -BRICK_Y_OFFSET-BRICK_ROWS*(BRICK_HEIGHT
                                                                +BRICK_SEP_V))
                self._score += a
                self._ball.negate_vy()
            
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
