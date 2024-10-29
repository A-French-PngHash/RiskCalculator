from PIL import ImageFont, Image, ImageDraw


im = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}/activity chart.jpg")

im.save(f"{os.path.dirname(os.path.abspath(__file__))}/output.png", "PNG")