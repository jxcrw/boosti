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
balls = space_balls('12345', (PHX, 0), BALL2, '-x') | \
        space_balls('A9876', (2, PHY), BALL2, '-y')

table_std.add_balls(balls)
table_std.save(__file__)
