from flask import Flask
app = Flask(__name__)

import os
import cv2
import argparse
from palettable import ColorPalette

# Construct argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, required=True,
                    help="Enter the filepath of the image you wish to "
                    "be made palettable.")
parser.add_argument("-n", "--number", type=int, default=5,
                    help="Enter the number of colors to include in the palette.")
parser.add_argument("-p", "--position", type=str, default='topRight',
                    help="Where would you like to place the palette?"
                    "Options: topRight, topLeft, bottomRight, bottomLeft")
parser.add_argument("-o", "--orientation", type=str, default='vert',
                    help="How would you like the palette oriented?"
                    "Options: vert = vertical, horz = horizontal")
parser.add_argument("-s", "--scale", type=float, default=0.3,
                    help="The size of the color blocks in the palette, relative to the image size")
args = vars(parser.parse_args())

# Use image provided to incorporate the image color palette onto the image
input = args['image']
num = args['number']
pos = args['position']
orient = args['orientation']
scale = args['scale']

output = os.path.join(os.path.expanduser('~'), "Desktop/")
print("Location of your palettable image:", output)
image = cv2.imread(input)
palettable = ColorPalette(image, n_sig=num, position=pos, orient=orient, size=scale)
palettable.show_image_with_palette(output)
