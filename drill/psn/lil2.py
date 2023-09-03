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
balls = {'cb': [(-2, 1), (-2, -1)]} | \
        space_balls('13579', (-1, PHY), BALL2, '-y') | \
        space_balls('2468A', (-1, NHY), BALL2, '+y')

table_std.add_balls(balls)
table_std.save(__file__)
