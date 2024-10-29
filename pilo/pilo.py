import os
from PIL import ImageFont, Image, ImageDraw




'''
bases impérial?
vaisseaux?

'''

dirName= os.path.dirname(os.path.abspath(__file__))
im = Image.new("RGB", (20000, 20000), "white")
titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=20)
draw = ImageDraw.Draw(im)
tab = tableau(1, 0, 0, 2, 1, 0)

draw.text((100, 100), f"Nombre de vaisseaux capitaux du joueur 1 : {tab.nb_vaisseaux_capitaux_j1}", font=generalFont, fill=(0, 0, 0))
draw.text((200, 100), f"Nombre de vaisseaux capitaux du joueur 2 : {tab.nb_vaisseaux_capitaux_j2}", font=generalFont, fill=(0, 0, 0))
draw.text((300, 100), f"Nombre de chasseurs du joueur 1 : {tab.nb_chasseurs_j1}", font=generalFont, fill=(0, 0, 0))
draw.text((400, 100), f"Nombre de chasseurs du joueur 2 : {tab.nb_chasseurs_j1}", font=generalFont, fill=(0, 0, 0))
draw.text((500, 100), f"Nombre de bombardiers du joueur 1 : {tab.nb_bombardiers_j1}", font=generalFont, fill=(0, 0, 0))
draw.text((600, 100), f"Nombre de bombardiers du joueur 2 : {tab.nb_bombardiers_j2}", font=generalFont, fill=(0, 0, 0))


def drawTable(valueList):
    tablexpos = 1000
    tableypos = 100
    hauteurCellule = 200
    largeurCellule = 200
    for i in range(len(valueList) + 1):
        ypos = tableypos + i * hauteurCellule
        draw.line([(tablexpos, ypos), (tablexpos + largeurCellule * 3, ypos)], fill=(0, 0, 0))

    for i in range(4):
        xpos = tablexpos + i * largeurCellule
        draw.line([(xpos, tableypos), (xpos, tableypos + hauteurCellule * len(valueList))], fill=(0, 0, 0))

    for i, line in enumerate(valueList):
        for j, column in enumerate(row):
            xpos = tablexpos + j * largeurCellule + cell_padding
            ypos = tableypos + i * hauteurCellule + cell_padding
            draw.text((xpos, ypos), str(cell), fill=(0, 0, 0), font=font)

#drawTable()

im.save(f"{dirName}/output.png", "PNG")