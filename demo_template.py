#!/usr/bin/env python3
from PIL import Image
from demoOp import demoOp
from imgen import *

def runOperationOnFile(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage( tex(inputFile, "RGB"), width, height, outputFile )

if __name__ == "__main__":
    demoOp(runOperationOnFile, "test", "test function")
