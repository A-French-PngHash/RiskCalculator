from math import floor
from PIL import Image, ImageDraw
import sys
from pilo.fonts import *
sys.path.append(f'{dirName}/../')
from classes import Tableau, Configuration, Case

class ImageDrawingService:
    draw : ImageDraw

    def draw_data(self, tab: Tableau, finaldir : str, finalname: str):
        """
        Draws and saves an image displaying the data contained in `tab`.

        Parameters:
            - config : Initial configuration (number of ships...)
            - tab : Instance of Tableau containing the data to display.
            - finaldir : Directory where the image should be saved.
            - finalname : How the image should be named. Note : the extension will be .png.
            WARNING : Will overide an image if it already exists under the same name.
        """
        im = Image.new("RGB", (max(500, 110+ 100*len(tab.liste_proba[0])), max(500, 305 + 100*len(tab.liste_proba))), "white")
        self.draw = ImageDraw.Draw(im)
            

        self.draw.multiline_text((im.width / 2 - 160, 5), "Attaque", font=bigBigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 - 160, 50), f"Capital: {tab.config.vaisseaux_att[0]}\nBombardier: {tab.config.vaisseaux_att[1]}\nChasseur: {tab.config.vaisseaux_att[2]}", font=bigGeneralFont, fill=(0, 0, 0))

        self.draw.multiline_text((im.width / 2 + 160, 5), "Défense", font=bigBigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 + 160,50), f"Capital: {tab.config.vaisseaux_def[0]}\nBombardier: {tab.config.vaisseaux_def[1]}\nChasseur: {tab.config.vaisseaux_def[1]}\nBase: {'Oui' if tab.config.base else 'Non'}", font=bigGeneralFont, fill=(0, 0, 0))
        self.drawTable(5,200,tab.liste_proba)

        im.save(f"{finaldir}/{finalname}.png", "PNG")

    def _drawFirstTile(self, width, height, x0, y0):
        self.draw.line((x0, y0, x0 + width, y0 + height), fill = (0, 0, 0), width=1)
        print()
        self.draw.text(
            xy=(x0 + width * 0.1, y0 + height * 0.75), 
            text="Attaque", 
            font=generalFont, 
            fill = (0, 0, 0))
        
        self.draw.text(
            xy=(x0 + width * 0.3, y0 + height * 0.02), 
            text="Defense", 
            font=generalFont, 
            fill = (0, 0, 0))


    def drawTable(self, tablexpos:int,tableypos:int,valueList:list):
        hauteurCellule = 100
        largeurCellule = 100
        margeInterieure = 50
        x0 = tablexpos
        y0 = tableypos

        # Dessine les couleurs
        # Première ligne
        for i in range(len(valueList[0]) + 1):    
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            if i == 0:
                self._drawFirstTile(largeurCellule, hauteurCellule, x0, y0)
            else:
                couleur =  (255,255,255)
                self.draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            x0 += largeurCellule

        #Première colonne
        x0 = tablexpos
        y0 = tableypos + hauteurCellule
        for j in range(len(valueList[0]) - 1):
            couleur = (255,255,255)
            x1 = x0 + largeurCellule
            y1 = y0 + hauteurCellule
            self.draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            y0 += hauteurCellule
        
        x0 = tablexpos + largeurCellule
        y0 = tableypos + hauteurCellule
        for i,liste in enumerate(valueList):
            for j,case in enumerate(liste):
                x1 = x0 + largeurCellule
                y1 = y0 + hauteurCellule
                if case.proba > 0.5:
                    couleur = (0,255,0)
                elif case.proba <0.5:
                    couleur = (255,0,0)
                else:
                    couleur = (255,165,0)
                self.draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
                x0 += largeurCellule
            y0 += hauteurCellule
            x0 = tablexpos + largeurCellule

        
        #Dessine les lignes du tableau
        for i in range(len(valueList)+2):
            ypos = tableypos + i * hauteurCellule
            self.draw.line([(tablexpos, ypos), (tablexpos + largeurCellule * (len(valueList[0]) + 1), ypos)], fill=(0, 0, 0))
        for i in range(len(valueList[0])+2):
            xpos = tablexpos + i * largeurCellule
            self.draw.line([(xpos, tableypos), (xpos, tableypos + hauteurCellule * (len(valueList) + 1))], fill=(0, 0, 0))

        #Ecris les valeurs dans l'image
        for i in range(len(valueList[0])):
            xpos = tablexpos + largeurCellule + i * largeurCellule + 45
            ypos = tableypos + 30
            self.draw.text((xpos, ypos), str(i+1), fill=(0,0,0), font=bigGeneralFont)
        
        for j in range(len(valueList)):
            xpos = tablexpos + 45
            ypos = tableypos + hauteurCellule + j * hauteurCellule + 30
            self.draw.text((xpos, ypos), str(j+1), fill=(0,0,0), font=bigGeneralFont)

        for i, line in enumerate(valueList):
            for j, column in enumerate(line):
                xpos = tablexpos + largeurCellule + j * largeurCellule + 10
                ypos = tableypos + hauteurCellule + i * hauteurCellule + 30
                self.draw.text((xpos, ypos), str(round(column.proba, 3)*100)+"%", fill=(0,0,0), font=bigGeneralFont)


tempConf = Configuration([2,3,3],[2,3,3],True)
tempCase = Case(0.7,5)
service = ImageDrawingService()
cases =  [tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase]
service.draw_data(Tableau(tempConf,[cases, cases, cases]),dirName,"output")