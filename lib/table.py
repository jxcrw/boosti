#!/usr/bin/env python3
"""Pool table"""

from PIL import Image

from utils import d2p, BALLS


class Table:
    """A pool table."""
    def __init__(self):
        # Load up images.
        self.table = Image.open(r'..\_img\table.png')
        self.balls = BALLS

    def add_ball(self, ball: str, pos: (float, float)) -> None:
        """Add a ball to the table at a given position (in diamonds)."""
        ball = self.balls[ball]
        self.table.paste(ball, d2p(*pos), mask=ball)

    def show(self) -> None:
        self.table.show()


if __name__ == '__main__':
    table = Table()
    table.show()
