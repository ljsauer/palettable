import os
import cv2
import argparse
from palettable import ColorPalette

# Construct argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-image", type=str, required=True,
                    help="Enter the filepath of the image you wish to "
                    "be made palettable.")
args = vars(parser.parse_args())

# Use image provided to incorporate the image color palette onto the image
input = args['image']
output = os.path.join(os.environ["USERPROFILE"], "Desktop/")
image = cv2.imread(input)
palettable = ColorPalette(image, n_sig=10, position='topRight', orient='vert')
palettable.show_image_with_palette(output)
