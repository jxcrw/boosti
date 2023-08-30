#!/usr/bin/env python3
"""big1 drill"""

import random
from utils import *

table_ref = Image.open(r"..\_img\table.png")
table_dyn = Image.open(r"..\_img\table.png")

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Reference
# └─────────────────────────────────────────────────────────────────────────────
table_ref.paste(ball_7g, d2p(-2.5, 0), mask=ball_7g)
table_ref.paste(ball_7, d2p(-2, 0), mask=ball_7)
table_ref.paste(ball_7g, d2p(-1.5, 0), mask=ball_7g)

table_ref.paste(ball_8g, d2p(2.5, 0), mask=ball_8g)
table_ref.paste(ball_8, d2p(2, 0), mask=ball_8)
table_ref.paste(ball_8g, d2p(1.5, 0), mask=ball_8g)

table_ref.paste(ball_9g, d2p(-0.5, 0), mask=ball_9g)
table_ref.paste(ball_9, d2p(0, 0), mask=ball_9)
table_ref.paste(ball_9g, d2p(0.5, 0), mask=ball_9g)

table_ref.show()

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Dynamic
# └─────────────────────────────────────────────────────────────────────────────
range_7 = [-2.5, -2, -1.5]
range_8 = [1.5, 2, 2.5]
range_9 = [-0.5, 0, 0.5]

table_dyn.paste(ball_7, d2p(random.choice(range_7), 0), mask=ball_7)
table_dyn.paste(ball_8, d2p(random.choice(range_8), 0), mask=ball_8)
table_dyn.paste(ball_9, d2p(random.choice(range_9), 0), mask=ball_9)

table_dyn.show()
