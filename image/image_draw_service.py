from PIL import Image, ImageDraw
if __name__=="__main__":
    from fonts import *
else:
    from image.fonts import *
import sys
from image.vector import Vector
sys.path.append(f'{dirName}/../')
from classes import Tableau, Configuration, Case

class ImageDrawingService:
    draw : ImageDraw
    use_gradient: bool = True
    green = Vector([137, 255, 107])
    red = Vector([255, 62, 62])
    hauteurCellule = 100
    largeurCellule = 100

    def draw_data(self, tab: Tableau, finaldir : str, finalname: str, use_gradient : bool):
        """
        Draws and saves an image displaying the data contained in `tab`.

        Parameters:
            - config : Initial configuration (number of ships...)
            - tab : Instance of Tableau containing the data to display.
            - finaldir : Directory where the image should be saved.
            - finalname : How the image should be named. Note : the extension will be .png.
            WARNING : Will overide an image if it already exists under the same name.
        """
        self.use_gradient = use_gradient
        im = Image.new("RGB", (max(1000, 110+ self.largeurCellule*(len(tab.liste_proba[0]))+1), max(500, 305 + self.hauteurCellule*(len(tab.liste_proba) + 1))), "white")
        self.draw = ImageDraw.Draw(im)
            
        att_def_distance = 400
        offset = -60

        distance_column = 180
        # Attack configuration
        self.draw.multiline_text((im.width / 2 - att_def_distance / 2 + offset, 5), "Attaque", font=bigBigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 - att_def_distance / 2 + offset - distance_column / 2, 50), f"Capital: {tab.config.vaisseaux_att[0]}\nBombardier: {tab.config.vaisseaux_att[1]}\nChasseur: {tab.config.vaisseaux_att[2]}", font=bigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 - att_def_distance / 2 + offset + distance_column / 2, 50), f"Min Soldiers: {tab.config.attack_stop_condition}", font=bigGeneralFont, fill=(0, 0, 0))

        # Defense configuration
        self.draw.multiline_text((im.width / 2 + att_def_distance / 2 + offset, 5), "Défense", font=bigBigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 + att_def_distance / 2 - distance_column/2 + offset,50), f"Capital: {tab.config.vaisseaux_def[0]}\nBombardier: {tab.config.vaisseaux_def[1]}\nChasseur: {tab.config.vaisseaux_def[2]}", font=bigGeneralFont, fill=(0, 0, 0))
        self.draw.multiline_text((im.width / 2 + att_def_distance / 2 + distance_column / 2 + offset,50), f"Base: {'Yes' if tab.config.base else 'No'}\nDeath Star: {'Yes' if tab.config.death_star else 'No'}\nAttack Bonus: {tab.config.death_star_fight_bonus}", font=bigGeneralFont, fill=(0, 0, 0))
        
        self.drawTable((im.size[0] - self.largeurCellule * (len(tab.liste_proba[0]) + 1 ))/2,200,tab.liste_proba, tab.config)

        im.save(f"{finaldir}/{finalname}.png", "PNG")

    def _get_color(self, percentage) -> Vector:
        """
        Returns the color to put in the tile depending on the percentage given.
        """
        if self.use_gradient:
            return (percentage * self.green + (1 - percentage) * self.red)
        else:
            if percentage > 0.50:
                return self.green
            elif percentage < 0.50:
                return self.red
            else:
                return (self.green + self.red) / 2
            

    def _drawFirstTile(self, width, height, x0, y0):
        self.draw.line((x0, y0, x0 + width, y0 + height), fill = (0, 0, 0), width=1)
        
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


    def drawTable(self, tablexpos:int,tableypos:int,valueList:list, configuration : Configuration):
        x0 = tablexpos
        y0 = tableypos

        # Dessine les couleurs
        # Première ligne
        for i in range(len(valueList[0]) + 1):    
            x1 = x0 + self.largeurCellule
            y1 = y0 + self.hauteurCellule
            if i == 0:
                self._drawFirstTile(self.largeurCellule, self.hauteurCellule, x0, y0)
            else:
                couleur =  (255,255,255)
                self.draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            x0 += self.largeurCellule

        #Première colonne
        x0 = tablexpos
        y0 = tableypos + self.hauteurCellule
        for j in range(len(valueList[0]) - 1):
            couleur = (255,255,255)
            x1 = x0 + self.largeurCellule
            y1 = y0 + self.hauteurCellule
            self.draw.rectangle([x0, y0, x1, y1], fill=couleur, outline=couleur)
            y0 += self.hauteurCellule
        
        x0 = tablexpos + self.largeurCellule
        y0 = tableypos + self.hauteurCellule
        for i,liste in enumerate(valueList):
            for j,case in enumerate(liste):
                if i >= configuration.attack_stop_condition:
                    x1 = x0 + self.largeurCellule
                    y1 = y0 + self.hauteurCellule
                    self.draw.rectangle([x0, y0, x1, y1], fill=self._get_color(case.proba).int_tupple_cords, outline=couleur)
                    x0 += self.largeurCellule
            y0 += self.hauteurCellule
            x0 = tablexpos + self.largeurCellule

        
        #Dessine les lignes du tableau
        for i in range(len(valueList)+2):
            ypos = tableypos + i * self.hauteurCellule
            self.draw.line([(tablexpos, ypos), (tablexpos + self.largeurCellule * (len(valueList[0]) + 1), ypos)], fill=(0, 0, 0))
        for i in range(len(valueList[0])+2):
            xpos = tablexpos + i * self.largeurCellule
            self.draw.line([(xpos, tableypos), (xpos, tableypos + self.hauteurCellule * (len(valueList) + 1))], fill=(0, 0, 0))

        #Ecris les valeurs dans l'image
        for i in range(len(valueList[0])):
            xpos = tablexpos + self.largeurCellule + i * self.largeurCellule + 45
            ypos = tableypos + 30
            self.draw.text((xpos, ypos), str(i+1), fill=(0,0,0), font=bigGeneralFont)
        
        for j in range(len(valueList)):
            xpos = tablexpos + 45
            ypos = tableypos + self.hauteurCellule + j * self.hauteurCellule + 30
            self.draw.text((xpos, ypos), str(j+1), fill=(0,0,0), font=bigGeneralFont)

        for i, line in enumerate(valueList):
            for j, column in enumerate(line):
                x,y = tablexpos + self.largeurCellule + j * self.largeurCellule, tableypos + self.hauteurCellule + i * self.hauteurCellule
                # (x,y) is the top corner of the cell
                xcenter, ycenter = x + self.largeurCellule / 2, y + self.hauteurCellule / 2
                
                if i >= configuration.attack_stop_condition:
                    self.draw.text((xcenter - 30, ycenter - 15), str(round(round(column.proba, 3)*100,3))+"%", fill=(0,0,0), font=bigGeneralFont)
                else:
                    self._draw_diagonale_case(x, y)
    
    def _draw_diagonale_case(self, x, y):
        third_l = self.largeurCellule / 3
        third_h = self.hauteurCellule / 3
        self.draw.line((x + third_l, y, x, y + third_h), fill = (0, 0, 0), width=1)
        self.draw.line((x + 2*third_l, y, x, y + 2*third_h), fill = (0, 0, 0), width=1)
        
        self.draw.line((x + self.largeurCellule, y + third_h, x + third_l, y + self.hauteurCellule), fill = (0, 0, 0), width=1)
        self.draw.line((x + self.largeurCellule, y + 2*third_h, x + 2*third_l, y + self.hauteurCellule), fill = (0, 0, 0), width=1)
        
        # Diagonale
        self.draw.line((x + self.largeurCellule, y, x, y + self.hauteurCellule), fill = (0, 0, 0), width=1)



if __name__=="__main__":
    tempConf = Configuration([2,3,3],[2,3,3],True)
    tempCase = Case(0.7,5)
    service = ImageDrawingService()
    cases =  [tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase,tempCase]
    service.draw_data(Tableau(tempConf,[cases, cases, cases]),dirName,"output",True)
