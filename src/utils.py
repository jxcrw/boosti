#!/usr/bin/env python3
"""Utilities for generating table diagrams"""


from PIL import Image

BALL = 0.18  # Diamonds

def d2p(diamonds_x: float, diamonds_y: float) -> (int, int):
    """Convert diamond units to pixels."""
    pixels_x = diamonds_x * 1200 + 564
    pixels_y = diamonds_y * 1200 + 564
    return (int(pixels_x), int(pixels_y))

print(d2p(2, 2))
print(d2p(4, 2))
print(d2p(6, 2))

# Opening the primary image (used in background)
table = Image.open(r"C:\~\dev\pool\_img\table.png")

# Opening the secondary image (overlay image)
ball = Image.open(r"C:\~\dev\pool\_img\ball_ghost.png")

# Pasting img2 image on top of table
# starting at coordinates (0, 0)
table.paste(ball, d2p(0 + BALL/2, 0), mask = ball)
table.paste(ball, d2p(0 + BALL/2, 1), mask = ball)
table.paste(ball, d2p(0 + BALL/2, 2), mask = ball)
table.paste(ball, d2p(0 + BALL/2, 3), mask = ball)
table.paste(ball, d2p(0 + BALL/2 + BALL, 0), mask = ball)
table.paste(ball, d2p(0 + BALL/2 + BALL, 1), mask = ball)
table.paste(ball, d2p(0 + BALL/2 + BALL, 2), mask = ball)
table.paste(ball, d2p(0 + BALL/2 + BALL, 3), mask = ball)

table.paste(ball, d2p(2, 2), mask = ball)
table.paste(ball, d2p(2, 2 - BALL), mask = ball)
table.paste(ball, d2p(4, 2), mask = ball)
table.paste(ball, d2p(4, 2 - BALL), mask = ball)
table.paste(ball, d2p(6, 2), mask = ball)
table.paste(ball, d2p(6, 2 - BALL), mask = ball)

# Displaying the image
table.show()
