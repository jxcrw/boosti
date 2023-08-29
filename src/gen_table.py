#!/usr/bin/env python3
"""Blank table template"""


from PIL import Image

# Opening the primary image (used in background)
img1 = Image.open(r"blank2.png")

# Opening the secondary image (overlay image)
img2 = Image.open(r"ball_cue.png")

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, (1341, 741), mask = img2)
img1.paste(img2, (1395, 741), mask = img2)
img1.paste(img2, (168, 1314), mask = img2)

# Displaying the image
img1.show()
