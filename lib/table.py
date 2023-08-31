#!/usr/bin/env python3
"""Pool table"""

from pathlib import Path
import random

from lib.utils import BALLS, DIR_DYN, TABLE, diamond2pixel


class Table:
    """A pool table."""
    def __init__(self):
        self.table = TABLE.copy()

    def add_ball(self, ball: str, pos: (float, float)) -> None:
        """Add a ball at the given position."""
        ball = BALLS[ball]
        pos_px = diamond2pixel(*pos)
        self.table.paste(ball, pos_px, mask=ball)

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

    def add_dyn_balls(self, dyn_balls: dict[str, tuple[list]]) -> None:
        """Add multiple dynamic balls at random positions."""
        for dyn_ball, choices in dyn_balls.items():
            self.add_dyn_ball(dyn_ball, *choices)

    def show(self) -> None:
        """Display the table."""
        self.table.show()

    def save(self, path: str) -> None:
        """Render the table to the appropriate output directory based on the given path."""
        path = path.replace(r'.py', r'.png')
        path = path.replace(r'drill', r'_img/drill')
        self.table.save(path)
        print(Path(path))

    def save_dyn(self, path: str) -> None:
        """Render the table to the dynamic directory based on the given path."""
        name = Path(path).stem
        path = f'{DIR_DYN}/{name}_dyn.png'
        self.table.save(path)
        print(Path(path))


if __name__ == '__main__':
    table = Table()
    table.show()
