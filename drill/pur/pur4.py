#!/usr/bin/env python3
"""Drill"""

from lib.table import Table
from lib.utils import BALL, N1X, NFY, P1X

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {
    'gb': [(0, 0), (0 - BALL, 0), (0 + BALL, 0)],
    'cb': [(-1, NFY), (1, NFY)],
    'b1': [((0 - BALL * 2) - BALL * 0, 0)],
    'b3': [((0 - BALL * 2) - BALL * 2, 0)],
    'b5': [((0 - BALL * 2) - BALL * 4, 0)],
    'b7': [((0 - BALL * 2) - BALL * 6, 0)],
    'b9': [((0 - BALL * 2) - BALL * 8, 0)],
    'b2': [((0 + BALL * 2) + BALL * 0, 0)],
    'b4': [((0 + BALL * 2) + BALL * 2, 0)],
    'b6': [((0 + BALL * 2) + BALL * 4, 0)],
    'b8': [((0 + BALL * 2) + BALL * 6, 0)],
    'b10': [((0 + BALL * 2) + BALL * 8, 0)],
}
table_std.add_balls(balls)
table_std.save(__file__)