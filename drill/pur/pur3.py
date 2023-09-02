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
    'cb': [(-3, NFY), (3, NFY)],
    'b1': [(N1X + BALL * 0, 0)],
    'b3': [(N1X + BALL * 2, 0)],
    'b5': [(N1X + BALL * 4, 0)],
    'b7': [(N1X + BALL * 6, 0)],
    'b9': [(N1X + BALL * 8, 0)],
    'b2': [(P1X - BALL * 0, 0)],
    'b4': [(P1X - BALL * 2, 0)],
    'b6': [(P1X - BALL * 4, 0)],
    'b8': [(P1X - BALL * 6, 0)],
    'b10': [(P1X - BALL * 8, 0)],
}
table_std.add_balls(balls)
table_std.save(__file__)