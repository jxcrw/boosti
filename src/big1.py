#!/usr/bin/env python3
"""big1 drill"""

import random
from table import Table


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
table_ref = Table()
table_dyn = Table()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Reference
# └─────────────────────────────────────────────────────────────────────────────
table_ref.add_ball('b7', (-2, 0))
table_ref.add_ball('b7g', (-2.5, 0))
table_ref.add_ball('b7g', (-1.5, 0))

table_ref.add_ball('b8', (2, 0))
table_ref.add_ball('b8g', (2.5, 0))
table_ref.add_ball('b8g', (1.5, 0))

table_ref.add_ball('b9', (0, 0))
table_ref.add_ball('b9g', (-0.5, 0))
table_ref.add_ball('b9g', (0.5, 0))

table_ref.show()


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Dynamic
# └─────────────────────────────────────────────────────────────────────────────
range_7 = [-2.5, -2, -1.5]
range_8 = [1.5, 2, 2.5]
range_9 = [-0.5, 0, 0.5]

table_dyn.add_ball('b7', (random.choice(range_7), 0))
table_dyn.add_ball('b8', (random.choice(range_8), 0))
table_dyn.add_ball('b9', (random.choice(range_9), 0))

table_dyn.show()
