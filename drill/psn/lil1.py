#!/usr/bin/env python3
"""Drill"""

from lib.table import Table
from lib.utils import BALL, PHX, PHY

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {
    'b1': [(PHX - BALL * 0, 0)],
    'b2': [(PHX - BALL * 2, 0)],
    'b3': [(PHX - BALL * 4, 0)],
    'b4': [(PHX - BALL * 6, 0)],
    'b5': [(PHX - BALL * 8, 0)],
    'b6': [(2, PHY - BALL * 8)],
    'b7': [(2, PHY - BALL * 6)],
    'b8': [(2, PHY - BALL * 4)],
    'b9': [(2, PHY - BALL * 2)],
    'b10': [(2, PHY - BALL * 0)],
}
table_std.add_balls(balls)
table_std.save(__file__)
