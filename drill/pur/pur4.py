#!/usr/bin/env python3
"""Drill"""

from lib.common import *
from lib.table import Table
from lib.utils import space_balls

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {'cb': [(-1, NFY), (1, NFY)]} | \
        {'gb': [(0, 0), (0 - BALL, 0), (0 + BALL, 0)]} | \
        space_balls('13579', (0 - HBALL * 4, 0), BALL2, '-x') | \
        space_balls('2468A', (0 + HBALL * 4, 0), BALL2, '+x')

table_std.add_balls(balls)
table_std.save(__file__)
