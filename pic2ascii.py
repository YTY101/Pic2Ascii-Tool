import utils
import gscale
import math
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', default= 0.43, dest='scale', required=False)
    parser.add_argument('--out', default='out.txt', dest='outFile', required=False)
    parser.add_argument('--cols', default='100', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action="store_true")

    args = parser.parse_args()

    if args.outFile:
        f = open(args.outFile, 'w')
        asciiimg = utils.convertImage2Ascii(args.imgFile, int(args.cols), float(args.scale), args.moreLevels)  
        for c in asciiimg:
            f.write(c)
    
    f.close()
    print("Ascii image has been writen to " + args.imgFile)

if __name__ == '__main__':
    main()