import os
from PIL import ImageFont, Image, ImageDraw




'''
bases impérial?
vaisseaux?

'''

dirName= os.path.dirname(os.path.abspath(__file__))
im = Image.new("RGB", (2000, 2000), "white")
titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=20)
draw = ImageDraw.Draw(im)

def drawTable():
    xbegin = 50
    ybegin = 50
    for i in range(10):
        for j in range(10):
            draw.text((xbegin+i*50, ybegin+j*50), "Hello", font=generalFont, fill=(0, 0, 0))

drawTable()

im.save(f"{dirName}/output.png", "PNG")