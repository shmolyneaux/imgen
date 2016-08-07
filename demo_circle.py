#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    genImage(thresh(radialGradient(50,50,40,(255,255,255), (0,0,0) ),
                    (1,1,1)),
             100, 100, "out/circle.png", mode="RGB" )
