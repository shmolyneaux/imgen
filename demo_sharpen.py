#!/usr/bin/env python3
from PIL import Image
from demoOp import demoOp
from imgen import *

def runOperationOnFile(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage(conv( tex(inputFile, "RGB"), [[ 0,-1, 0],
                                           [-1, 5,-1],
                                           [ 0,-1, 0]]),
             width, height, outputFile )

if __name__ == "__main__":
    demoOp(runOperationOnFile, "sharpen", "sharpen")
