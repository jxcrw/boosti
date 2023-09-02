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
DIR_ROOT = sys.path[1]
DIR_IMG = f'{DIR_ROOT}/_img'
DIR_DYN = f'{DIR_ROOT}/_train'
DIR_DRILL = f'{DIR_ROOT}/drill'
DRILLS = []
for root, dirs, files in os.walk(DIR_DRILL):
    files = [f'{root}/{f}' for f in files if '.py' in f]
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

# Dimensions in diamonds (standard unit for app)
BALL = BALL_INCH / DIAMOND_INCH
HBALL = BALL / 2

# Common ball positions
PFX = 4 - HBALL
NFX = -PFX
PFY = 2 - HBALL
NFY = -PFY
PHX = 4 - BALL
NHX = -PHX
PHY = 2 - BALL
NHY = -PHY
P1X = 4 - BALL * 3 / 2
N1X = -P1X
P1Y = 2 - BALL * 3 / 2
N1Y = -P1Y


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Images
# └─────────────────────────────────────────────────────────────────────────────
IMG_TABLE = Image.open(rf'{DIR_IMG}/table/table.png')

IMG_BALLS = {}
balls_meta = ['cb', 'gb', 'cbg', 'gbg']
balls_object = [f'b{num}' for num in range(1, 16)]
balls_ghost = [f'b{num}g' for num in range(1, 16)]
balls_all = balls_meta + balls_object + balls_ghost
for ball in balls_all:
    IMG_BALLS[ball] = Image.open(rf'{DIR_IMG}/ball/{ball}.png')


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
