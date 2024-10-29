import os
from PIL import ImageFont, Image, ImageDraw
import sys
dirName= os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{dirName}/../')
from classes import Tableau, Configuration

config = Configuration([2,3,3],[2,3,3],True)
tab = Tableau(config,[[0.2,5.0],[0.1,5.0]])
im = Image.new("RGB", (500 + 100*len(tab.liste_proba), 500+100*len(tab.liste_proba)), "white")

titleFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-ExtraBold.otf",
size=30)
generalFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=15)
bigGeneralFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=23)
bigBigGeneralFont = ImageFont.truetype(f"{dirName}/Marianne/Marianne-Regular.otf", size=33)
draw = ImageDraw.Draw(im)

def drawTable(tablexpos,tableypos,valueList):
    hauteurCellule = 100
    largeurCellule = 100
    margeInterieure = 50
    x0 = tablexpos
    y0 = tableypos

    # Dessine les couleurs
    # Première ligne
    for i in range(len(valueList[0]) + 1):
            if i==0:
                couleur = (0,0,0)
            else:
                couleur = (255,255,255)
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            x0 += largeurCellule

    x0 = tablexpos
    y0 = tableypos + hauteurCellule
    for j in range(len(valueList[0]) - 1):
            couleur = (255,255,255)
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            y0 += hauteurCellule
    
    x0 = tablexpos + largeurCellule
    y0 = tableypos + hauteurCellule
    for i,liste in enumerate(valueList):
        for j,case in enumerate(valueList[0]):
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            if 1:#case.proba > 0.5:
                couleur = (0,255,0)
            elif 0:#case.proba <0.5:
                couleur = (255,0,0)
            else:
                couleur = (255,165,0)
            draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            x0 += largeurCellule
        y0 += hauteurCellule
        x0 = tablexpos + largeurCellule

    
    #Dessine les lignes
    for i in range(len(valueList)+2):
        ypos = tableypos + i * hauteurCellule
        draw.line([(tablexpos, ypos), (tablexpos + largeurCellule * (len(valueList[0]) + 1), ypos)], fill=(0, 0, 0))
    for i in range(len(valueList[0])+2):
        xpos = tablexpos + i * largeurCellule
        draw.line([(xpos, tableypos), (xpos, tableypos + hauteurCellule * (len(valueList) + 1))], fill=(0, 0, 0))

    #Ecris
    for i in range(len(valueList)):
            xpos = tablexpos + largeurCellule + i * largeurCellule + 45
            ypos = tableypos + 30
            draw.text((xpos, ypos), str(i+1), fill=(0,0,0), font=bigGeneralFont)
    
    for j in range(len(valueList)):
            xpos = tablexpos + 45
            ypos = tableypos + hauteurCellule + j * hauteurCellule + 30
            draw.text((xpos, ypos), str(j+1), fill=(0,0,0), font=bigGeneralFont)

    for i, line in enumerate(valueList):
        for j, column in enumerate(line):
            xpos = tablexpos + largeurCellule + j * largeurCellule + 10
            ypos = tableypos + hauteurCellule + i * hauteurCellule + 30
            draw.text((xpos, ypos), str(round(column*100, 3))+"%", fill=(0,0,0), font=bigGeneralFont)

draw.multiline_text((5, 5), "Attaque", font=bigBigGeneralFont, fill=(0, 0, 0))
draw.multiline_text((5, 60), f"Capital: {tab.config.vaisseaux_att[0]}\nBombardier: {tab.config.vaisseaux_att[1]}\nChasseur: {tab.config.vaisseaux_att[2]}", font=bigGeneralFont, fill=(0, 0, 0))

draw.multiline_text((300, 5), "Défense", font=bigBigGeneralFont, fill=(0, 0, 0))
draw.multiline_text((300,60), f"Capital: {tab.config.vaisseaux_def[0]}\nBombardier: {tab.config.vaisseaux_def[1]}\nChasseur: {tab.config.vaisseaux_def[1]}", font=bigGeneralFont, fill=(0, 0, 0))

if tab.config.base:
    draw.multiline_text((300, 150), "Base: Oui", font=bigGeneralFont, fill=(0, 0, 0))
else:
    draw.multiline_text((300, 150), "Base: Non", font=bigGeneralFont, fill=(0, 0, 0))
drawTable(5,200,tab.liste_proba)

im.save(f"{dirName}/output.png", "PNG")