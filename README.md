# imgen
Personal playground for generating images in a functional style in Python. Not made to be fast...

## Currently supports
- Loading images
- Convolution operations (blurs, sharpening, edge detection)
- Masks
- Radial gradients
- Thresholding
- Layering
- Conversion to greyscale
- Inverting images
- ...and Stripes 


# Code Example
The following code snippet from `demo_wallpaper_small.py`:
```python
genImage(layer(constant(10,10,10,255),
               mask(radialGradient(240, 135, 160,
                                   (60,60,60,255),
                                   (20,20,20,255)),
                    pinStripe(1, 15, (255,255,255,255), (0,0,0,0)))),
         480, 270, "out/wallpaper_small.png")
```
Outputs:

![](https://github.com/WimbledonLabs/imgen/raw/master/out/wallpaper_small.png)

# Example Images
More examples can be found [in this directory](https://github.com/WimbledonLabs/imgen/tree/master/out). All examples can be generated using `demo.py`. Some of these demos can take a long time to execute.

### Original
![](https://github.com/WimbledonLabs/imgen/raw/master/out/baboon_test.png)


### Edge Detection
From `demo_edge_detect.py`
```python
def detectEdges(inputFile, outputFile):
    width, height = Image.open(inputFile).size
    genImage( conv(tex(inputFile, "RGB"), [[0, 1,0],
                                           [1,-4,1],
                                           [0, 1,0]]),
              width, height, outputFile )
```
![](https://github.com/WimbledonLabs/imgen/raw/master/out/baboon_edge.png)


### Sharpen
From `demo_sharpen.py`

![](https://github.com/WimbledonLabs/imgen/raw/master/out/baboon_sharpen.png)


### Gaussian Blur
From `demo_gaussian_blur.py`

![](https://github.com/WimbledonLabs/imgen/raw/master/out/baboon_gblur2.png)


### Mask
From `demo_mask.py`
```python
# Since shapes like circles aren't supported yet, we have to create them
# mathemagically by thresholding a radial gradient
circleMask = thresh(radialGradient(256, 256, 200, (255, 255, 255),
                                   (0,0,0)),
                    (1,1,1), pos=(255,255,255,255), neg=(255,255,255,0))

genImage(layer(tex("ref/boat.png", mode="RGBA"),
               mask(tex("ref/baboon.png", mode="RGBA"), 
                    circleMask)),
         512, 512, "out/mask2.png", mode="RGB" )

```
![](https://github.com/WimbledonLabs/imgen/raw/master/out/mask2.png)


### Invert
From `demo_inverse.py`

![](https://github.com/WimbledonLabs/imgen/raw/master/out/baboon_inverted.png)


## TODO
- 3D transformations
- Rotation
- Scaling
- Interpolation of images when transformed
- Converting existing function to better accept floating point arguments
- Change color scale from 0-255 to 0.0-1.0
- Less hardcoding of transparency (IE make the alpha channel not an edge case)
- GIF output
- Polygons / Contours / Other Shapes
- Lines
- Linear Gradient
- More primitive functions (multiplication, subtraction, etc.)
