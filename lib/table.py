#!/usr/bin/env python3
"""Pool table"""

from utils import d2p, BALLS, TABLE


class Table:
    """A pool table."""
    def __init__(self):
        self.table = TABLE.copy()

    def add_ball(self, ball: str, pos: (float, float)) -> None:
        """Add a ball to the table at a given position."""
        ball_img = BALLS[ball]
        self.table.paste(ball_img, d2p(*pos), mask=ball_img)

    def add_balls(self, balls: dict[str, list]) -> None:
        """Add multiple balls to the table at the given positions."""
        for ball, positions in balls.items():
            for pos in positions:
                self.add_ball(ball, pos)

    def show(self) -> None:
        """Display the table."""
        self.table.show()

    def save(self, path: str) -> None:
        """Save the table to the given path."""
        self.table.save(path)


if __name__ == '__main__':
    table = Table()
    table.show()
