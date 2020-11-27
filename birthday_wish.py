"""
This is the main code file.

Most of the code is written using python3 and the pillow library

One of the key resource for this code to come up is:
https://automatetheboringstuff.com/chapter17/
"""

import sys
from PIL import Image, ImageDraw, ImageFont
import os

try:

    from_name = input("Please enter your name: ")
    to_name = input("Happy birthday to?: ")
    to_name_file = "_".join(to_name.split())

    if from_name == "":
        from_name = ""
    if to_name == "":
        to_name = 'FRIEND!!'
        to_name_file = "birthday"

except Exception as e:
    to_name = 'FRIEND!!'
    to_name_file = "birthday"
    
print("\n")
print("\t\t****************************************************")
print("\t\t\t !!! HAPPY BIRTHDAY " + to_name + " !!!")
print("\t\t****************************************************")

pstrImg = Image.open('birthday_template.jpg')
# print(pstrImg.size)
draw = ImageDraw.Draw(pstrImg)

# The below config is for windows, for other operating systems
# On Windows: C:\Windows\Fonts
# On OS X: /Library/Fonts and /System/Library/Fonts
# On Linux: /usr/share/fonts/truetype 
fontsFolder = "C:\Windows\Fonts"
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 100)
draw.text((210, 547), to_name.upper(), fill=(255,61,177,128), font=arialFont)
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 40)
draw.text((570, 740), from_name.upper(), fill=(255,61,177,128), font=arialFont)

pstrImg.save(str(to_name_file) + '.png')
