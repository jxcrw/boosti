#!/usr/bin/env python3
"""Utilities for generating table diagrams"""

import sys
from PIL import Image

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Pathing
# └─────────────────────────────────────────────────────────────────────────────
DIR_ROOT = sys.path[1]
DIR_DYN = f'{DIR_ROOT}/_train'
DIR_IMG = f'{DIR_ROOT}/_img'


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Dimensions
# └─────────────────────────────────────────────────────────────────────────────
# Dimensions in inches
BALL_INCH = 2.25
DIAMOND_INCH = 12.5
RAIL_WIDTH_INCH = 7
SURFACE_WIDTH_INCH = 100
SURFACE_HEIGHT_INCH = 50

# Dimensions in pixels
DPI = 96
PX_PER_DIAMOND = DIAMOND_INCH * DPI
OFFSET_RAIL_PX = (RAIL_WIDTH_INCH - BALL_INCH / 2) * DPI
OFFSET_ORIGIN_X_PX = OFFSET_RAIL_PX + PX_PER_DIAMOND * 4
OFFSET_ORIGIN_Y_PX = OFFSET_RAIL_PX + PX_PER_DIAMOND * 2

# Dimensions in diamonds
BALL = BALL_INCH / DIAMOND_INCH
HBALL = BALL / 2

# Common ball positions
NFX = -4 + HBALL
PFX = 4 - HBALL
NFY = -2 + HBALL
PFY = 2 - HBALL
NHX = -4 + BALL
PHX = 4 - BALL
NHY = -2 + BALL
PHY = 2 - BALL
N1X = -4 + BALL * 3 / 2
P1X = 4 - BALL * 3 / 2
N1Y = -2 + BALL * 3 / 2
P1Y = 2 - BALL * 3 / 2


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Images
# └─────────────────────────────────────────────────────────────────────────────
TABLE = Image.open(rf'{DIR_IMG}/table/table.png')

BALLS = {}
balls_meta = ['cb', 'gb', 'cbg', 'gbg']
balls_object = [f'b{num}' for num in range(1, 16)]
balls_ghost = [f'b{num}g' for num in range(1, 16)]
balls_all = balls_meta + balls_object + balls_ghost
for ball in balls_all:
    BALLS[ball] = Image.open(rf'{DIR_IMG}/ball/{ball}.png')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helper Functions
# └─────────────────────────────────────────────────────────────────────────────
def diamond2pixel(xd: float, yd: float) -> (int, int):
    """Convert diamond units to pixels."""
    xp = OFFSET_ORIGIN_X_PX + xd * PX_PER_DIAMOND
    yp = OFFSET_ORIGIN_Y_PX + -yd * PX_PER_DIAMOND
    return int(xp), int(yp)
