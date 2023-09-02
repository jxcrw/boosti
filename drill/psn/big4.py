#!/usr/bin/env python3
"""Drill"""

import random

from lib.table import Table
from lib.utils import BALL, NFX, NHY, PFX, PHY

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()
table_dyn = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
range_x = [0.5 * mag for mag in range(1, 8)] + [-0.5 * mag for mag in range(1, 8)]
range_y = [PHY, 1.5, 1, -1, -1.5, NHY]
positions = []
for x in range_x:
    for y in range_y:
        pos = (x, y)
        positions.append(pos)

balls = {
    'gb': positions,
    'b1': [(2, 1.5)],
    'b2': [(2, -1.5)],
    'b3': [(-2, 1.5)],
    'b4': [(-2, -1.5)],
    'b5': [(NFX, BALL)],
    'b7': [(NFX, 0)],
    'b9': [(NFX, -BALL)],
    'b6': [(PFX, BALL)],
    'b8': [(PFX, 0)],
    'b10': [(PFX, -BALL)],
}
table_std.add_balls(balls)
table_std.save(__file__)


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Dynamic
# └─────────────────────────────────────────────────────────────────────────────
balls = ['b1', 'b2', 'b3', 'b4']
balls = random.sample(balls, 4)

range_x_neg = [-0.5 * mag for mag in range(1, 8)]
range_x_pos = [0.5 * mag for mag in range(1, 8)]
range_y_neg = [NHY, -1, -1.5]
range_y_pos = [1, 1.5, PHY]

top_left = [range_x_neg, range_y_pos]
top_right = [range_x_pos, range_y_pos]
btm_left = [range_x_neg, range_y_neg]
btm_right = [range_x_pos, range_y_neg]

dyn_balls = {
    balls[0]: top_left,
    balls[1]: top_right,
    balls[2]: btm_left,
    balls[3]: btm_right,
}
table_dyn.add_dyn_balls(dyn_balls)
table_dyn.save(__file__, is_dyn=True)
