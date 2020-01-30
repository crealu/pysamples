from PIL import Image, ImageFilter
from PIL import ImageFont, ImageDraw
from gradient_math import get_gradation_3d as gg3
import numpy as np
import os
import random

currentDir = os.getcwd()

img1 = Image.open(currentDir + '/img/foliage.jpg')

width = img1.size[0]
height = img1.size[1]

eachPixel = []
widthRange = range(0, width)

for w in widthRange:
    pixel = img1.getpixel((w, 10))
    eachPixel.append(pixel)

# gradient number
gn = 0

while gn < 5:
    random1 = eachPixel[random.randint(0, len(eachPixel))]
    random2 = eachPixel[random.randint(0, len(eachPixel))]

    array = gg3(512, 256, random1, random2, (True, True, True))
    newGradient = Image.fromarray(np.uint8(array))

    draw = ImageDraw.Draw(newGradient)
    font = ImageFont.truetype("Comfortaa[wght].ttf", 18)

    draw.text((10, 10), "Color 1: \n" + str(random1), (255, 255, 255), font=font)
    draw.text((380, 10), "Color 2: \n" + str(random2), (255, 255, 255), font=font)

    newGradient.show()
    keep = input('Keep this gradient? (y/n) ')

    if (keep is 'y'):
        newGradient.save(currentDir + '/gradients/random_gradient' + str(gn)  + '.jpg', quality=95)

    gn += 1
