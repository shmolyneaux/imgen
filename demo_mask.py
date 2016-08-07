#!/usr/bin/env python3
from PIL import Image
from imgen import *

if __name__ == "__main__":
    circleMask = thresh(radialGradient(256, 256, 200, (255, 255, 255),
                                       (0,0,0)),
                        (1,1,1), pos=(255,255,255,255), neg=(255,255,255,0))

    smallCircleMask = thresh(radialGradient(50, 50, 40, (255,255,255),
                                            (0,0,0)),
                             (1,1,1),
                             pos=(255,255,255,255),
                             neg=(255,255,255,0))

    genImage(layer(constant(0, 0, 0, 255),
                   mask(pinStripe(2, 10, (0xff, 0x66, 0x00, 0xff),
                                          (0x20, 0x20, 0x20, 0xff)), 
                        smallCircleMask)),
             100, 100, "out/mask.png", mode="RGB" )

    genImage(layer(tex("ref/boat.png", mode="RGBA"),
                   mask(tex("ref/baboon.png", mode="RGBA"), 
                        circleMask)),
             512, 512, "out/mask2.png", mode="RGB" )
