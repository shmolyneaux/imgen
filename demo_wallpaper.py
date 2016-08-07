#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    genImage(layer(constant(10,10,10,255),
                   mask(radialGradient(1920/2, 1080/2, 650,
                                       (40,40,40,255),
                                       (20,20,20,255)),
                        pinStripe(1, 15, (255,255,255,255), (0,0,0,0)))),
             1920, 1080, "out/wallpaper.png")
