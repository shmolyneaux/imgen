from standard_images import *

"""
f takes in 2 strings, an input file name and an output file name
- f is expected to write to the output file name after performing some operation
  on the image from the input file
"""
def demoOp(f, operationSuffix, friendlyName):
    OUT_DIR = "out"
    for filename in ref_image_list:
        print("Running %s on %s" % (friendlyName, filename))
        path = ref_image_dir + "/" + filename
        name, dot, filetype = filename.partition(".")
        outputPath = "%s/%s_%s.%s" % (OUT_DIR, name, operationSuffix, filetype)
        f(path, outputPath)
        print("Image output to %s" % outputPath)
