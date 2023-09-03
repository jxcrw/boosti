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
balls = {'cb': [(-2, 0)]} | \
        space_balls('13579', (0, P1Y), BALL2, '-y') | \
        space_balls('2468A', (0, N1Y), BALL2, '+y')

table_std.add_balls(balls)
table_std.save(__file__)
