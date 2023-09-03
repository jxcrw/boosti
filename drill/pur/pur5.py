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
balls = MIGHTY_X
table_std.add_balls(balls)
table_std.save(__file__)
