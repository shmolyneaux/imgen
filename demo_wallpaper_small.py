#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    genImage(layer(constant(10,10,10,255),
                   mask(radialGradient(240, 135, 160,
                                       (60,60,60,255),
                                       (20,20,20,255)),
                        pinStripe(1, 15, (255,255,255,255), (0,0,0,0)))),
             480, 270, "out/wallpaper_small.png")
