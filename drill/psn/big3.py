#!/usr/bin/env python3
"""Drill"""

from lib.table import Table
from lib.utils import NHX, PHX

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
    'b6': [(3, 0)],
    'b8': [(PHX, 0)],
    'b5': [(-2, 0)],
    'b7': [(-3, 0)],
    'b9': [(NHX, 0)],
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