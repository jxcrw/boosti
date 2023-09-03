#!/usr/bin/env python3
"""Drill"""

from lib.common import *
from lib.table import Table

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {
    'cb': [(-2, 1), (-2, -1)],
    'b1': [(0, 0)],
    'b3': [(NFX, HBALL + BALL * 3)],
    'b5': [(NFX, HBALL + BALL * 2)],
    'b7': [(NFX, HBALL + BALL * 1)],
    'b9': [(NFX, HBALL + BALL * 0)],
    'b2': [(NFX, -HBALL - BALL * 4)],
    'b4': [(NFX, -HBALL - BALL * 3)],
    'b6': [(NFX, -HBALL - BALL * 2)],
    'b8': [(NFX, -HBALL - BALL * 1)],
    'b10': [(NFX, -HBALL - BALL * 0)]
}
table_std.add_balls(balls)
table_std.save(__file__)
