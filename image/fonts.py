from PIL import ImageFont
import os

dirName= os.path.dirname(os.path.abspath(__file__))

titleFont = ImageFont.truetype(
    f"{dirName}/Marianne/Marianne-ExtraBold.otf",
    size=30
    )

generalFont = ImageFont.truetype(
    f"{dirName}/Marianne/Marianne-Regular.otf", 
    size=15
)

bigGeneralFont = ImageFont.truetype(
    f"{dirName}/Marianne/Marianne-Regular.otf", 
    size=23
)

bigBigGeneralFont = ImageFont.truetype(
    f"{dirName}/Marianne/Marianne-Regular.otf", 
    size=33
)
