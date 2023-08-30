#!/usr/bin/env python3
"""Utilities for generating table diagrams"""

from PIL import Image

BALL_INCH = 2.25
DIAMOND_INCH = 12.5
RAIL_WIDTH_INCH = 7
SURFACE_WIDTH_INCH = 100
SURFACE_HEIGHT_INCH = 50

DPI = 96
OFFSET_OUTLINE_PX = 5
OFFSET_ORIGIN_PX = (RAIL_WIDTH_INCH - BALL_INCH / 2) * DPI
DIAMOND_PX = DIAMOND_INCH * DPI


def d2p(diamonds_x: float, diamonds_y: float) -> (int, int):
    """Convert diamond units to pixels."""
    pixels_x = OFFSET_ORIGIN_PX + DIAMOND_PX * 4 + diamonds_x * DIAMOND_PX
    pixels_y = OFFSET_ORIGIN_PX + DIAMOND_PX * 2 + -diamonds_y * DIAMOND_PX
    return int(pixels_x), int(pixels_y)


# Open images
table = Image.open(r"..\_img\table.png")
ball = Image.open(r"..\_img\ball_ghost.png")


# Define ball positions
top_left = d2p(-4, 2)
top_cent = d2p(0, 2)
top_ryit = d2p(4, 2)
mid_left = d2p(-4, 0)
mid_cent = d2p(0, 0)
mid_ryit = d2p(4, 0)
btm_left = d2p(-4, -2)
btm_cent = d2p(0, -2)
btm_ryit = d2p(4, -2)
print(top_left)
print(top_cent)
print(top_ryit)
print(mid_left)
print(mid_cent)
print(mid_ryit)
print(btm_left)
print(btm_cent)
print(btm_ryit)


# Paste image on table
table.paste(ball, top_left, mask=ball)
table.paste(ball, top_cent, mask=ball)
table.paste(ball, top_ryit, mask=ball)
table.paste(ball, mid_left, mask=ball)
table.paste(ball, mid_cent, mask=ball)
table.paste(ball, mid_ryit, mask=ball)
table.paste(ball, btm_left, mask=ball)
table.paste(ball, btm_cent, mask=ball)
table.paste(ball, btm_ryit, mask=ball)


# Display image
table.show()
