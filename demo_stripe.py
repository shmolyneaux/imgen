#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    genImage(pinStripe(2, 10, (255,0,0), (0,0,255)),
             100, 100, "out/stripes.png", mode="RGB" )
