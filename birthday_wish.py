import sys
from PIL import Image, ImageDraw, ImageFont
import os

try:
    arg_ls = [arg for arg in sys.argv]
    to_name = " ".join(arg_ls[1:])
    to_name_file = "_".join(arg_ls[1:])

    if to_name == "":
        to_name = 'TO YOU'
        to_name_file = "birthday"

except Exception as e:
    to_name = 'TO YOU'
    to_name_file = "birthday"
    
print("\n")
print("\t\t****************************************************")
print("\t\t\t !!! HAPPY BIRTHDAY " + to_name + " !!!")
print("\t\t****************************************************")

pstrImg = Image.open('birthday_template.jpg')
# print(pstrImg.size)
draw = ImageDraw.Draw(pstrImg)
fontsFolder = "C:\Windows\Fonts"
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 100)
draw.text((210, 547), to_name.upper(), fill=(255,61,177,128), font=arialFont)

pstrImg.save(str(to_name_file) + '.png')
