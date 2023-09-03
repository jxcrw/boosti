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
balls = {'cb': [(-1.5, 0)]} | \
        space_balls('13579', (1, P1Y), BALL2, '-y') | \
        space_balls('2468A', (1, N1Y), BALL2, '+y')

table_std.add_balls(balls)
table_std.save(__file__)
