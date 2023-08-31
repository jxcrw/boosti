#!/usr/bin/env python3
"""Utilities for generating table diagrams"""

from PIL import Image

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Table Dimensions
# └─────────────────────────────────────────────────────────────────────────────
BALL_INCH = 2.25
DIAMOND_INCH = 12.5
RAIL_WIDTH_INCH = 7
SURFACE_WIDTH_INCH = 100
SURFACE_HEIGHT_INCH = 50

DPI = 96
OFFSET_OUTLINE_PX = 5
OFFSET_ORIGIN_PX = (RAIL_WIDTH_INCH - BALL_INCH / 2) * DPI
DIAMOND_PX = DIAMOND_INCH * DPI


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Ball Images
# └─────────────────────────────────────────────────────────────────────────────
BALLS = {}
balls_meta = ['cb', 'gb']
balls_object = [f'b{num}' for num in range(1, 16)]
balls_ghost = [f'b{num}g' for num in range(1, 16)]
balls_all = balls_meta + balls_object + balls_ghost
for ball in balls_all:
    BALLS[ball] = Image.open(rf'..\_img\{ball}.png')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helper Functions
# └─────────────────────────────────────────────────────────────────────────────
def d2p(diamonds_x: float, diamonds_y: float) -> (int, int):
    """Convert diamond units to pixels."""
    pixels_x = OFFSET_ORIGIN_PX + DIAMOND_PX * 4 + diamonds_x * DIAMOND_PX
    pixels_y = OFFSET_ORIGIN_PX + DIAMOND_PX * 2 + -diamonds_y * DIAMOND_PX
    return int(pixels_x), int(pixels_y)
