#!/usr/bin/env python3
from PIL import Image
from demoOp import demoOp
from imgen import *

def runOperationOnFile(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage(gaussianBlur(tex(inputFile, "RGB"), 2), 
             width, height, outputFile)

if __name__ == "__main__":
    demoOp(runOperationOnFile, "gblur2", "gaussian blur where size=2")
