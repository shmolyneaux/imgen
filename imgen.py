import math
from PIL import Image

def gridIter(xMax, yMax, xMin=0, yMin=0):
    for x in range(xMin, xMax):
        for y in range(yMin, yMax):
            yield (x,y)

def genImage(f, xSize, ySize, name, mode="RGBA", default=(0,0,0,0)):
    im = Image.new(mode, (xSize, ySize), default)
    px = im.load()

    for (x,y) in gridIter(xSize, ySize):
        px[x,y] = f(x,y)
    im.save(name)

def conv(f, table):
    # table in square and has to have odd length dimensions
    def innerConv(x,y):
        offset = int(len(table)/2)
        c = [0]*len(f(x,y)) # We don't know how large the vector is, so we have
                            # to get that information from the function at some
                            # point
        for (dx,dy) in gridIter(1+offset, 1+offset,
                                 -offset,  -offset):
            fc = f(x+dx, y+dy)
            for channel in range(len(c)):
                weight = table[dy+offset][dx+offset]
                c[channel] += weight*fc[channel]

        for channel in range(len(c)):
            c[channel] = int(c[channel])
        return tuple(c)

    return innerConv

def normConv(f, table):
    return conv(f, normalizeMatrix(table))

def zeroMatrix(size=1):
    matrix = []
    for x in range(size*2+1):
        l = []
        for y in range(size*2+1):
            l.append(0)
        matrix.append(l)
    return matrix

def normalizeMatrix(abnormal):
    weight = sum(sum(abnormal, [])) # O(n^2) complexity, for small n

    # Create a new list since we don't want to modify the contents of the
    # matrix passed in
    m = []
    for x in range(len(abnormal)):
        l = []
        for y in range(len(abnormal[x])):
            l.append( abnormal[y][x] / weight )
        m.append(l)
    return m

def gaussianMatrix(size=1, variance=1):
    matrix = zeroMatrix(size)
    for (x,y) in gridIter(1+size, 1+size,
                           -size,  -size):
        val = math.exp(-(x**2+y**2)/(2*variance)) / (2 * math.pi * variance)
        matrix[x+size][y+size] = val
    return normalizeMatrix(matrix)

def gaussianBlur(f, size=1, variance=1):
    m = gaussianMatrix(size, variance)
    return normConv(f, m)

def boxBlur(f, size=1):
    w = 1.0/((size+2)**2)
    table = [[w]*(size*2+1)]*(size*2+1) # This creates a matrix which contains
                                        # copies of the same list, which is
                                        # okay because everything in them is the
                                        # same
    return conv(f, table)

def pinStripe(thickness, space, fgc, bgc):
    def innerStripe(x, y):
        return fgc if (x+y) % space < thickness else bgc

    return innerStripe

def offset(f, ox, oy):
    def innerOffset(x, y):
        return f(x-ox, y-oy)

    return innerOffset

def mul(f, factor):
    def innerMul(x,y):
        c = list(f(x,y))
        for channel in range(len(c)):
            c[channel] *= factor[channel]

        return tuple(c)

    return innerMul

def diff(a, b):
    def innerDiff(x,y):
        ca = a(x,y)
        cb = b(x,y)
        c = [0]*len(ca)
        for channel in range(len(c)):
            c[channel] = int((ca[channel] - cb[channel]) / 2 + 127)
        return tuple(c)

    return innerDiff

def tex(fileName, mode=None, default=None):
    im = Image.open(fileName)
    if mode:
        im = im.convert(mode)

    px = im.load()

    if not default:
        default = tuple( [0]*len(px[0,0]) )

    def innerTex(x,y):
        try:
            return px[x,y]
        except IndexError:
            return default

    return innerTex

def constant(*color):
    def innerConstant(x,y):
        return tuple(color)

    return innerConstant

def radialGradient(cx, cy, r, innerColor, outerColor):
    def innerRadialGradient(x, y):
        dx = cx - x
        dy = cy - y
        d = math.sqrt(dx**2 + dy**2)
        t = max( 0, min(1, (r - d)/float(r)) )
        c = [0]*len(innerColor)
        for i in range(len(c)):
            c[i] = int(round(innerColor[i]*t + outerColor[i]*(1-t)))

        return tuple(c)

    return innerRadialGradient

def layer(base, *args):
    def innerLayer(x, y):
        c = list(base(x,y))
        for f in args:
            p = f(x, y)
            alpha = 255
            if len(p) == 4:
                alpha = p[3]
                c[3] = int(round( c[3] - c[3]*alpha/255 + alpha ))
            for i in range(3):
                c[i]  = int(round(c[i] * (255 - alpha) / 255))
                c[i] += int(round(p[i] *         alpha / 255))
        return tuple(c)

    return innerLayer

def mask(f, m):
    def innerMask(x, y):
        mask = m(x, y)
        color = list(f(x, y))
        for channel in range(len(mask)):
            color[channel] = color[channel]*mask[channel]/255
        return tuple(color)

    return innerMask

def thresh(f, c, pos = (255,255,255,255), neg=(0,0,0,255)):
    def innerThresh(x, y):
        r = f(x, y)
        for channel in range(len(r)):
            if r[channel] < c[channel]:
                return neg
        else:
            return pos

    return innerThresh

def inv(f):
    def innerInv(x, y):
        c = list(f(x,y))
        for channel in range(len(c)):
            c[channel] = 255 - c[channel]
        return tuple(c)

    return innerInv

#def rotate(f, angle, origin=(0,0)):
#   pass

#def scale(f, s, origin(0,0)):
#   pass

#def threeDimensionalTransform(f, matrix):
#   pass

#def add(f, summand):
#   pass

#def sub(f, subtrahend):
#   pass

#def div(f, divisor):
#   pass

#def pow(f, exponent):
#   pass

#def linearTween(what?):
#   pass

#def sinTween(what?):
#   pass

#def linearGradient(p1, p2, c1, c2):
#   pass

#def noise(frequency, seed=None):
#   pass
