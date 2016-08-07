#!/usr/bin/env python3
from PIL import Image
from demoOp import demoOp
from imgen import *

W =  [[ 5,-3,-3],
      [ 5, 0,-3],
      [ 5,-3,-3]]

NW = [[ 5, 5,-3],
      [ 5, 0,-3],
      [-3,-3,-3]]

N =  [[ 5, 5, 5],
      [-3, 0,-3],
      [-3,-3,-3]]

NE = [[-3, 5, 5],
      [-3, 0, 5],
      [-3,-3,-3]]

E =  [[-3,-3, 5],
      [-3, 0, 5],
      [-3,-3, 5]]

SE = [[-3,-3,-3],
      [-3, 0, 5],
      [-3, 5, 5]]

S =  [[-3,-3,-3],
      [-3, 0,-3],
      [ 5, 5, 5]]

SW = [[-3,-3,-3],
      [ 5, 0,-3],
      [ 5, 5,-3]]

def runOperationOnFile(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage(layer(constant(0,0,0,255),
                   thresh(conv(tex(inputFile, mode="LA"), SW),
                          (384,0),
                          pos=(  0,  0,255,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), S),
                          (384,0),
                          pos=(  0,255,  0,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), SE),
                          (384,0),
                          pos=(  0,255,255,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), E),
                          (384,0),
                          pos=(255,  0,  0,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), NE),
                          (384,0),
                          pos=(255,  0,255,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), N),
                          (384,0),
                          pos=(255,255,  0,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), NW),
                          (384,0),
                          pos=(255,255,255,255),
                          neg=(  0,  0,  0,  0)),
                   thresh(conv(tex(inputFile, mode="LA"), W),
                          (384,0),
                          pos=(127,127,127,255),
                          neg=(  0,  0,  0,  0))),
             width, height, outputFile, mode="RGBA")

if __name__ == "__main__":
    demoOp(runOperationOnFile, "kirsch", "kirsch edge detection (very slow)")
