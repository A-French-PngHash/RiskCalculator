from PIL import ImageFont, Image, ImageDraw




'''
bases impérial?
vaisseaux?

'''

dirName= os.path.dirname(os.path.abspath(__file__))
im = Image.new("RGB", (2000, 2000), "white")
title_font = ImageFont.truetype(f"{dirName}/Fonts/Uni Sans Heavy.otf",
size=30)
body_font = ImageFont.truetype(f"{dirName}/Fonts/Uni Sans Thin.otf", size=20)
draw = ImageDraw.Draw(im)


im.save(f"{dirName}/output.png", "PNG")