import os
from PIL import ImageFont, Image, ImageDraw
import sys
dirName= os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{dirName}/../')
from classes import Tableau, Configuration

config = Configuration([2,3,3],[2,3,3],True)
tab = Tableau(config,[[0.2,5.0],[0.1,5.0]])
im = Image.new("RGB", (1000*len(tab.liste_proba), 1000*len(tab.liste_proba)), "white")

titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=20)
bigGeneralFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=40)

draw = ImageDraw.Draw(im)

def drawTable(tablexpos,tableypos,valueList):
    hauteurCellule = 100
    largeurCellule = 100
    margeInterieure = 10
    for i,liste in enumerate(valueList):
        for j,case in enumerate(valueList[0]):
            x0 = tablexpos + j * largeurCellule
            y0 = tableypos + i * hauteurCellule
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            if 1:#case.proba > 0.5:
                couleur = (0,255,0)
            elif 0:#case.proba <0.5:
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
            draw.text((xpos, ypos), str(round(column, 3)), fill=(0,0,0), font=generalFont)

draw.multiline_text((10, 10), f"Attaque\n Capital: {tab.config.vaisseaux_att[0]}\n Bombardier: {tab.config.vaisseaux_att[1]}\n Chasseur: {tab.config.vaisseaux_att[2]}", font=bigGeneralFont, fill=(0, 0, 0))
draw.multiline_text((1000, 10), f"Défense\n  Capital: {tab.config.vaisseaux_def[0]}\n Bombardier: {tab.config.vaisseaux_def[1]}\n Chasseur: {tab.config.vaisseaux_def[1]}", font=bigGeneralFont, fill=(0, 0, 0))

drawTable(100,100,tab.liste_proba)

im.save(f"{dirName}/output.png", "PNG")