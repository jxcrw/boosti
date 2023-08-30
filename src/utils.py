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
# table = Image.open(r"..\_img\table.png")
ball_cue = Image.open(r"..\_img\ball_cue.png")
ball_1 = Image.open(r"..\_img\ball_1.png")
ball_2 = Image.open(r"..\_img\ball_2.png")
ball_3 = Image.open(r"..\_img\ball_3.png")
ball_4 = Image.open(r"..\_img\ball_4.png")
ball_5 = Image.open(r"..\_img\ball_5.png")
ball_6 = Image.open(r"..\_img\ball_6.png")
ball_7 = Image.open(r"..\_img\ball_7.png")
ball_8 = Image.open(r"..\_img\ball_8.png")
ball_9 = Image.open(r"..\_img\ball_9.png")
ball_10 = Image.open(r"..\_img\ball_10.png")
ball_11 = Image.open(r"..\_img\ball_11.png")
ball_12 = Image.open(r"..\_img\ball_12.png")
ball_13 = Image.open(r"..\_img\ball_13.png")
ball_14 = Image.open(r"..\_img\ball_14.png")
ball_15 = Image.open(r"..\_img\ball_15.png")
ball_ghost = Image.open(r"..\_img\ball_ghost.png")

ball_cueg = Image.open(r"..\_img\ball_cueg.png")
ball_1g = Image.open(r"..\_img\ball_1g.png")
ball_2g = Image.open(r"..\_img\ball_2g.png")
ball_3g = Image.open(r"..\_img\ball_3g.png")
ball_4g = Image.open(r"..\_img\ball_4g.png")
ball_5g = Image.open(r"..\_img\ball_5g.png")
ball_6g = Image.open(r"..\_img\ball_6g.png")
ball_7g = Image.open(r"..\_img\ball_7g.png")
ball_8g = Image.open(r"..\_img\ball_8g.png")
ball_9g = Image.open(r"..\_img\ball_9g.png")
ball_10g = Image.open(r"..\_img\ball_10g.png")
ball_11g = Image.open(r"..\_img\ball_11g.png")
ball_12g = Image.open(r"..\_img\ball_12g.png")
ball_13g = Image.open(r"..\_img\ball_13g.png")
ball_14g = Image.open(r"..\_img\ball_14g.png")
ball_15g = Image.open(r"..\_img\ball_15g.png")
ball_ghostg = Image.open(r"..\_img\ball_ghostg.png")




# # Define ball positions
# top_left = d2p(-4, 2)
# top_cent = d2p(0, 2)
# top_ryit = d2p(4, 2)
# mid_left = d2p(-4, 0)
# mid_cent = d2p(0, 0)
# mid_ryit = d2p(4, 0)
# btm_left = d2p(-4, -2)
# btm_cent = d2p(0, -2)
# btm_ryit = d2p(4, -2)
# print(top_left)
# print(top_cent)
# print(top_ryit)
# print(mid_left)
# print(mid_cent)
# print(mid_ryit)
# print(btm_left)
# print(btm_cent)
# print(btm_ryit)
#
#
# # Paste image on table
# table.paste(ball, top_left, mask=ball)
# table.paste(ball, top_cent, mask=ball)
# table.paste(ball, top_ryit, mask=ball)
# table.paste(ball, mid_left, mask=ball)
# table.paste(ball, mid_cent, mask=ball)
# table.paste(ball, mid_ryit, mask=ball)
# table.paste(ball, btm_left, mask=ball)
# table.paste(ball, btm_cent, mask=ball)
# table.paste(ball, btm_ryit, mask=ball)
#
#
# # Display image
# table.show()
