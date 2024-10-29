import os
from PIL import ImageFont, Image, ImageDraw
from classes import tableau, Configuration


dirName= os.path.dirname(os.path.abspath(__file__))
config = Configuration([2,3,3],[2,3,3],True,50,50)
tab = tableau(config,[["qejkfdgs","dsfds"],["dsfds","sfsf"]])
im = Image.new("RGB", (1000*len(tab.liste_proba), 1000*len(tab.liste_proba)), "white")
titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=20)
draw = ImageDraw.Draw(im)

draw.text((100, 100), f"Nombre de vaisseaux capitaux de l'attaquant : {str(config.vaisseaux_j1[0])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 150), f"Nombre de vaisseaux capitaux du défenseur : {str(config.vaisseaux_j2[0])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 200), f"Nombre de chasseurs de l'attaquant : {str(config.vaisseaux_j1[2])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 250), f"Nombre de chasseurs du défenseur : {str(config.vaisseaux_j2[2])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 300), f"Nombre de bombardiers de l'attaquant : {str(config.vaisseaux_j1[1])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 350), f"Nombre de bombardiers du défenseur : {str(config.vaisseaux_j2[1])}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 400), f"Nombre de troupes de l'attaquant : {str(config.nb_troupes_j1)}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 450), f"Nombre de troupes du défenseur : {str(config.nb_troupes_j2)}", font=generalFont, fill=(0, 0, 0))
draw.text((100, 500), f"Y a-t-il une base ? : {str(config.base)}", font=generalFont, fill=(0, 0, 0))


def drawTable(valueList):
    tablexpos = 100
    tableypos = 550
    hauteurCellule = 100
    largeurCellule = 100
    margeInterieure = 10

    #Dessine les fonds
    for i in range(len(valueList)):
        for j in range(len(valueList[0])):
            x0 = tablexpos + j * largeurCellule
            y0 = tableypos + i * hauteurCellule
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            if 1>0.5:
                couleur = (0,255,0)
            elif 1<0.5:
                couleur = (255,0,0)
            else:
                couleur = (255,165,0)
            draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)

    #Dessine les lignes
    for i in range(len(valueList)+1):
        ypos = tableypos + i * hauteurCellule
        draw.line([(tablexpos, ypos), (tablexpos + largeurCellule * len(valueList[0]), ypos)], fill=(0, 0, 0))
    for i in range(len(valueList[0])+1):
        xpos = tablexpos + i * largeurCellule
        draw.line([(xpos, tableypos), (xpos, tableypos + hauteurCellule * len(valueList))], fill=(0, 0, 0))

    #Ecris
    for i, line in enumerate(valueList):
        for j, column in enumerate(line):
            xpos = tablexpos + j * largeurCellule + margeInterieure
            ypos = tableypos + i * hauteurCellule + margeInterieure
            draw.text((xpos, ypos), str(column), fill=(0,0,0), font=generalFont)

drawTable(tab.liste_proba)

im.save(f"{dirName}/output.png", "PNG")