# Pic2Ascii-Tool
A simple tool which turns a picture into an ascii text

## Requirements
* pillow
## How to use it 
* --file: Name of the image you want to convert
* --out: Output filename (a txt file) (default: out.txt)
* --cols: Num of cols of the output ascii picture (kind o resolution, but should not be larger than cols of actual picture) (default: 100)
* --scale: The ratio of cols to rows (defaut: 0.43)
* --morelevels: Present the image in a more layered way
## Examples
* `python .\pic2ascii.py --file image.jpg`
* `python .\pic2ascii.py --file image.jpg --out high_resolution.txt --cols 500 --morelevels`
