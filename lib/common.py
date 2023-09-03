#!/usr/bin/env python3
"""Common game constants"""

from lib.utils import BALL_INCH, DIAMOND_INCH, space_balls

# Common widths (in diamonds)
BALL = BALL_INCH / DIAMOND_INCH
BALL2 = BALL * 2
HBALL = BALL / 2
DIAMOND = 1

# Common ball positions
PFX = 4 - HBALL
PFY = 2 - HBALL
PHX = 4 - BALL
PHY = 2 - BALL
P1X = 4 - HBALL * 3
P1Y = 2 - HBALL * 3
NFX = -PFX
NFY = -PFY
N1X = -P1X
N1Y = -P1Y
NHX = -PHX
NHY = -PHY

# Common ball groups
MIGHTY_X = {'cb': [(-2, -1), (2, -1)], 'b1': [(2, 1)], 'b2': [(-2, 1)]} | \
           space_balls('3579', (1 - BALL, PFY), BALL, '-x') | \
           space_balls('468A', (-1 + BALL, PFY), BALL, '+x')
