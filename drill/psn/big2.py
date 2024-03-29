#!/usr/bin/env python3
"""Drill"""

from lib.common import *
from lib.table import Table

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_std = Table()
table_dyn = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Standard
# └─────────────────────────────────────────────────────────────────────────────
balls = {
    'b4': [(2, 0)],
    # 'b4g': [(1.5, 0), (2.5, 0)],
    'b6': [(2, 1)],
    # 'b6g': [(1.5, 1), (2.5, 1)],
    'b8': [(2, PHY)],
    # 'b8g': [(1.5, PHY), (2.5, PHY)],
    'b5': [(-2, 0)],
    # 'b5g': [(-2.5, 0), (-1.5, 0)],
    'b7': [(-2, -1)],
    # 'b7g': [(-2.5, -1), (-1.5, -1)],
    'b9': [(-2, NHY)],
    # 'b9g': [(-2.5, NHY), (-1.5, NHY)],
}
table_std.add_balls(balls)
table_std.save(__file__)


# # ┌─────────────────────────────────────────────────────────────────────────────
# # │ Dynamic
# # └─────────────────────────────────────────────────────────────────────────────
# dyn_balls = {
#     'b4': ([1.5, 2, 2.5], [0]),
#     'b6': ([1.5, 2, 2.5], [1]),
#     'b8': ([1.5, 2, 2.5], [PHY]),
#     'b5': ([-1.5, -2, -2.5], [0]),
#     'b7': ([-1.5, -2, -2.5], [-1]),
#     'b9': ([-1.5, -2, -2.5], [NHY]),
# }
# table_dyn.add_dyn_balls(dyn_balls)
# table_dyn.save_dyn(__file__)
