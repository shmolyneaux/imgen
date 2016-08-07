#!/usr/bin/env python3
from PIL import Image
from demoOp import demoOp
from imgen import *

def runOperationOnFile(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage( inv(tex(inputFile, "RGB")), width, height, outputFile )

if __name__ == "__main__":
    demoOp(runOperationOnFile, "inverted", "invert colors")
