import sys
from PIL import Image, ImageDraw, ImageFont
import os

# draw a gray cross over an image
# with Image.open("zophie.jpg") as im:

#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)

#     # write to stdout
#     im.save("zop.jpg")

pstrImg = Image.open('birthday1_orig.jpg')
# print(pstrImg.size)
draw = ImageDraw.Draw(pstrImg)
fontsFolder = "C:\Windows\Fonts"
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 100)
draw.text((210, 547), 'JENNIFER', fill=(255,61,177,128), font=arialFont)

pstrImg.save('birthday1.png')