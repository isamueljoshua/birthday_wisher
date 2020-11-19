import sys
from PIL import Image, ImageDraw, ImageFont
import os

try:
    # arg_ls = [arg for arg in sys.argv]
    # to_name = " ".join(arg_ls[1:])
    # to_name_file = "_".join(arg_ls[1:])

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
fontsFolder = "C:\Windows\Fonts"
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 100)
draw.text((210, 547), to_name.upper(), fill=(255,61,177,128), font=arialFont)
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'CURLZ___.ttf'), 40)
draw.text((570, 740), from_name.upper(), fill=(255,61,177,128), font=arialFont)

pstrImg.save(str(to_name_file) + '.png')
