#!/usr/bin/env python3
"""Drill"""

from lib.common import *
from lib.table import Table
from lib.utils import space_balls

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()
table_dyn = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {'cb': [(-3, 1), (-3, -1)]} | \
        space_balls('12345', (-2, 0), DIAMOND, '+x')

table_std.add_balls(balls)
table_std.save(__file__)
