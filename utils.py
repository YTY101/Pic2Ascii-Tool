from PIL import Image
import numpy as np
from gscale import Gscale

def getRows(image, cols, scale):
    #image = Image.open(fileName).convert("L")
    W, H = image.size[0], image.size[1]
    w = W/cols
    h = w/scale

    return int(H/h), (w, h)    

def getAverageL(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))

def convertImage2Ascii(fileName, cols, scale, moreLevels = False):
    gscale = Gscale()
    gs = gscale.scale1 if moreLevels else gscale.scale2
    
    img = Image.open(fileName).convert('L')
    rows, patch_size = getRows(img, cols, scale)
    w, h = patch_size

    print("cols = %d, rows = %d" % (cols, rows))
    print("patchsize = %d x %d" % patch_size)
    
    if cols > img.size[0] or rows > img.size[1]:
        print("Image is too small for specified cols!")
        exit(0)
    
    asciiimg = []
    avgLs = []
    for j in range(rows):
        y1 = j * h
        y2 = img.size[1] if j == rows - 1 else (j + 1) * h
        for i in  range(cols):        
            x1 = i * w
            x2 = img.size[0] if i == cols - 1 else (i + 1) * w    
            avgL = getAverageL(img.crop((x1, y1, x2, y2)))
            asciiimg.append(gs[int((avgL/255) * (len(gs) - 1))])
        asciiimg.append('\n')
    return asciiimg
    