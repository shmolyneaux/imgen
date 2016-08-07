from PIL import Image
from imgen import *
from demoOp import demoOp
import os
import subprocess

if __name__ == "__main__":
    files = os.listdir()
    pyFiles = [f for f in files if f.startswith("demo_") and f.endswith(".py")]

    for script in pyFiles:
        print("Executing %s" % script)
        subprocess.call("python3 %s" % script, shell=True)
