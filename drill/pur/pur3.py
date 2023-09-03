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
balls = {'cb': [(-3, NFY), (3, NFY)]} | \
        space_balls('13579', (N1X, 0), BALL2, '+x') | \
        space_balls('2468A', (P1X, 0), BALL2, '-x')

table_std.add_balls(balls)
table_std.save(__file__)
