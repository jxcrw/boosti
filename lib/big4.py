#!/usr/bin/env python3
"""Big4 pool drill"""

import random

x_positions = [0.1, 0.5, 1.0]
y_positions = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
orders = [1, 2, 3, 4]

order = random.sample(orders, 4)
top_left = (random.choice(x_positions), random.choice(y_positions), order[0])
top_right = (random.choice(x_positions), random.choice(y_positions), order[1])
btm_left = (random.choice(x_positions), random.choice(y_positions), order[2])
btm_right = (random.choice(x_positions), random.choice(y_positions), order[3])

print(top_left)
print(top_right)
print(btm_left)
print(btm_right)
