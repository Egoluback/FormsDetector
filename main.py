from PIL import Image, ImageDraw
from Detector import Detector

import random, sys, math, PIL

# open cmd and type
# python main.py *path_to_image* *fill_color*

IMAGE_PATH = ""
fillColor = [0, 0, 0]

for i in range(len(sys.argv)):
    if (i == 1):
        IMAGE_PATH = sys.argv[i]
    elif (i == 2):
        FILL_COLOR = list(map(int, sys.argv[i].split(",")))

if (IMAGE_PATH == ""):
    IMAGE_PATH = input("Input path to image: ")

detector = Detector(fillColor, IMAGE_PATH, [{"value": 70, "mode": "moreEquals"}, {"value": 70, "mode": "moreEquals"}, {"value": 150, "mode": "less"}], True)

detector.Main()