#!/usr/bin/env python3

import numpy as np
from PIL import Image

m = np.zeros([sol.ylim, sol.xlim], dtype=np.uint8)
for coor in sol.visited:
    m[coor[0]][coor[1]] = 255

array_2d = np.array(m)  # Your 2D array
img = Image.fromarray(array_2d.astype("uint8"))  # Convert to uint8 if necessary
img.save("output.png")  # Save the image
