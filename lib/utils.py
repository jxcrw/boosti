#!/usr/bin/env python3
"""Utilities for generating table diagrams"""

import multiprocessing as mp
import os
from pathlib import Path
import subprocess
import sys
import time

from PIL import Image


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Performance
# └─────────────────────────────────────────────────────────────────────────────
CORES_RESERVED = 2
CORES = max((mp.cpu_count() - CORES_RESERVED), 1)


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Pathing
# └─────────────────────────────────────────────────────────────────────────────
DIR_ROOT = Path(sys.path[1])
DIR_DRILL = DIR_ROOT / 'drill'
DIR_DYN = DIR_ROOT / '_train'
DIR_IMG = DIR_ROOT / '_img'
DIR_IMG_DRILL = DIR_IMG / 'drill'
DIR_IMG_TABLE = DIR_IMG / 'table'
DIR_IMG_BALLS = DIR_IMG / 'ball'

DRILLS = []
for root, dirs, files in os.walk(DIR_DRILL):
    files = [os.path.join(root, f) for f in files if '.py' in f]
    DRILLS.extend(files)


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Dimensions
# └─────────────────────────────────────────────────────────────────────────────
# Dimensions in inches
BALL_INCH = 2.25
DIAMOND_INCH = 12.5
RAIL_WIDTH_INCH = 7
SURFACE_WIDTH_INCH = 100
SURFACE_HEIGHT_INCH = 50

# Dimensions in pixels
DPI = 96
PX_PER_DIAMOND = DIAMOND_INCH * DPI
OFFSET_RAIL_PX = (RAIL_WIDTH_INCH - BALL_INCH / 2) * DPI
ORIGIN_X_PX = OFFSET_RAIL_PX + PX_PER_DIAMOND * 4
ORIGIN_Y_PX = OFFSET_RAIL_PX + PX_PER_DIAMOND * 2


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Images
# └─────────────────────────────────────────────────────────────────────────────
IMG_TABLE = Image.open(DIR_IMG_TABLE / 'table.png')

IMG_BALLS = {}
balls_meta = ['cb', 'gb', 'cbg', 'gbg']
balls_object = [f'b{n}' for n in range(1, 16)]
balls_ghost = [f'b{n}g' for n in range(1, 16)]
balls_all = balls_meta + balls_object + balls_ghost
for ball in balls_all:
    IMG_BALLS[ball] = Image.open(DIR_IMG_BALLS / f'{ball}.png')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helper Functions
# └─────────────────────────────────────────────────────────────────────────────
def diamond2pixel(pos: tuple[float, float]) -> tuple[int, int]:
    """Convert an (x, y) position from diamonds to pixels."""
    x_diamond, y_diamond = pos[0], pos[1]
    x_px = ORIGIN_X_PX + PX_PER_DIAMOND * x_diamond
    y_px = ORIGIN_Y_PX + PX_PER_DIAMOND * -y_diamond
    return int(x_px), int(y_px)


def render_drill(path: str) -> None:
    """Render the drill with the given path."""
    subprocess.call(path, shell=True)


def render_all_drills() -> None:
    """Render all drills (in parallel)."""
    print(f"Rendering {len(DRILLS)} drills...")
    start = time.time()
    pool = mp.Pool(processes=CORES)
    pool.map(render_drill, DRILLS)
    end = time.time()
    print(f"...finished in {end - start:0.2}s.")


if __name__ == '__main__':
    render_all_drills()
