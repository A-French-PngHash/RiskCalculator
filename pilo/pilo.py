from PIL import ImageFont, Image, ImageDraw

im = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}/activity chart.jpg")
title_font = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}/Fonts/Uni Sans Heavy.otf",
size=30)
body_font = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}/Fonts/Uni Sans Thin.otf", size=20)



im.save(f"{os.path.dirname(os.path.abspath(__file__))}/output.png", "PNG")