#!/usr/bin/env python3
"""Common game constants"""

from lib.utils import BALL_INCH, DIAMOND_INCH


# Common widths (in diamonds)
BALL = BALL_INCH / DIAMOND_INCH
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
B3579 = ['b3', 'b5', 'b7', 'b9']
B468A = ['b4', 'b6', 'b8', 'b10']
B13579 = ['b1', 'b3', 'b5', 'b7', 'b9']
B2468A = ['b2', 'b4', 'b6', 'b8', 'b10']
