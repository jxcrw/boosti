#!/usr/bin/env python3
"""Pool table"""

import random

from lib.utils import DIR_DRILL, DIR_DYN, DIR_IMG_DRILL, IMG_BALLS, IMG_TABLE, diamond2pixel


class Table:
    """A pool table."""
    def __init__(self):
        self.table = IMG_TABLE.copy()

    def add_ball(self, ball: str, pos: tuple[float, float]) -> None:
        """Add a ball at the given position."""
        ball_img = IMG_BALLS[ball]
        pos_px = diamond2pixel(pos)
        self.table.paste(ball_img, pos_px, mask=ball_img)

    def add_balls(self, balls: dict[str, list]) -> None:
        """Add multiple balls at the given positions."""
        for ball, positions in balls.items():
            for pos in positions:
                self.add_ball(ball, pos)

    def add_dyn_ball(self, dyn_ball: str, choices_x: list, choices_y: list) -> None:
        """Add a dynamic ball at a random position chosen from the given choices."""
        x = random.choice(choices_x)
        y = random.choice(choices_y)
        self.add_ball(dyn_ball, (x, y))

    def add_dyn_balls(self, dyn_balls: dict[str, list]) -> None:
        """Add multiple dynamic balls at random positions."""
        for dyn_ball, choices in dyn_balls.items():
            self.add_dyn_ball(dyn_ball, *choices)

    def save(self, path: str, is_dyn: bool = False) -> None:
        """Render the table to the appropriate output directory based on the given path."""
        dir_out = DIR_DYN if is_dyn else DIR_IMG_DRILL
        path = path.replace(str(DIR_DRILL), str(dir_out))
        path = path.replace('.py', '.png')
        self.table.save(path)
        print(path)

    def show(self) -> None:
        """Display the table."""
        self.table.show()


if __name__ == '__main__':
    table = Table()
    table.show()
