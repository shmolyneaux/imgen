#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    width, height = Image.open("ref/baboon.png").size
    genImage(diff(conv( tex("ref/baboon.png", "RGB"), [[ 0,-1, 0],
                                                  [-1, 5,-1],
                                                  [ 0,-1, 0]]),
                  tex("ref/baboon.png")),
             width, height, "out/diff.png")
