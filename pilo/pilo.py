import os
from PIL import ImageFont, Image, ImageDraw
from classes import tableau, Configuration


dirName= os.path.dirname(os.path.abspath(__file__))
im = Image.new("RGB", (20000, 20000), "white")
titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=20)
draw = ImageDraw.Draw(im)
config = Configuration([2,3,3],[2,3,3],True,50,50)
tab = tableau(config,liste_proba)

draw.text((100, 100), f"Nombre de vaisseaux capitaux du joueur 1 : {tab.Configuration.vaisseaux_j1[0]}", font=generalFont, fill=(0, 0, 0))
draw.text((200, 100), f"Nombre de vaisseaux capitaux du joueur 2 : {tab.Configuration.vaisseaux_j2[0]}", font=generalFont, fill=(0, 0, 0))
draw.text((300, 100), f"Nombre de chasseurs du joueur 1 : {tab.Configuration.vaisseaux_j1[2]}", font=generalFont, fill=(0, 0, 0))
draw.text((400, 100), f"Nombre de chasseurs du joueur 2 : {tab.Configuration.vaisseaux_j2[2]}", font=generalFont, fill=(0, 0, 0))
draw.text((500, 100), f"Nombre de bombardiers du joueur 1 : {tab.Configuration.vaisseaux_j1[1]}", font=generalFont, fill=(0, 0, 0))
draw.text((600, 100), f"Nombre de bombardiers du joueur 2 : {tab.Configuration.vaisseaux_j2[1]}", font=generalFont, fill=(0, 0, 0))
draw.text((700, 100), f"Nombre de troupes du joueur 1 : {tab.Configuration.nb_troupes_j1}", font=generalFont, fill=(0, 0, 0))
draw.text((800, 100), f"Nombre de troupes du joueur 2 : {tab.Configuration.nb_troupes_j2}", font=generalFont, fill=(0, 0, 0))
draw.text((900, 100), f"Y a-t-il une base ? : {str(tab.Configuration.base)}", font=generalFont, fill=(0, 0, 0))


def drawTable(valueList):
    tablexpos = 1500
    tableypos = 100
    hauteurCellule = 200
    largeurCellule = 200
    margeInterieure = 10

    #Dessine les lignes
    for i in range(len(valueList) + 1):
        ypos = tableypos + i * hauteurCellule
        draw.line([(tablexpos, ypos), (tablexpos + largeurCellule * 3, ypos)], fill=(0, 0, 0))
    for i in range(len(valueList[0])+1):
        xpos = tablexpos + i * largeurCellule
        draw.line([(xpos, tableypos), (xpos, tableypos + hauteurCellule * len(valueList))], fill=(0, 0, 0))

    #Ecris
    for i, line in enumerate(valueList):
        for j, column in enumerate(row):
            xpos = tablexpos + j * largeurCellule + margeInterieure
            ypos = tableypos + i * hauteurCellule + margeInterieure
            draw.text((xpos, ypos), str(cell), fill=(0, 0, 0), font=font)

drawTable(tab.tableau)

im.save(f"{dirName}/output.png", "PNG")