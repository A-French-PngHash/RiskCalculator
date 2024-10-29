# Computing : 

from classes import Tableau, Configuration
from proba_calc.proba_calc import RiskProbaCalculator
from pilo.pilo import ImageDrawingService
import os

dirName= os.path.dirname(os.path.abspath(__file__))


# Configuration
def config():

    nb_chasseurs_at = int(input("Nombre de chasseurs de l'attaquant :"))
    nb_chasseurs_de = int(input("Nombre de chasseurs du défenseur :"))
    nb_bombardiers_at = int(input("Nombre de bombardiers de l'attaquant :"))
    nb_bombardiers_de = int(input("Nombre de bombardiers du défenseur :"))
    nb_capitaux_at = int(input("Nombre de vaisseaux capitaux de l'attaquant :"))
    nb_capitaux_de = int(input("Nombre de vaisseaux capitaux du défenseur :"))
    base = input("Le défenseur a_t_il une base impériale ? Y/N :")
    if base=="Y":
        base = True
    else:
        base = False
    
    configuration = Configuration([nb_capitaux_at, nb_bombardiers_at, nb_chasseurs_at],[nb_capitaux_de, nb_bombardiers_de, nb_chasseurs_de], base)
    return configuration


if __name__=="__main__":
    #configuration = config()
<<<<<<< HEAD
    configuration = Configuration([0, 0, 0], [0, 0, 0], False)
    risk_prob = RiskProbaCalculator(configuration)
    tab = risk_prob.compute_all(5, 5)
    image = ImageDrawingService()
=======
    configuration = Configuration([2, 2, 2], [0, 0, 0], False)
    print("🏇 Calculating probabilities...")
    risk_prob = RiskProbaCalculator(configuration)
    tab = risk_prob.compute_all(5, 5)
    print("🧑‍🎨Generating image...")
    image = ImageDrawingService()

>>>>>>> refs/remotes/origin/main
    dir = f"{dirName}/output"
    if not os.path.exists(dir):
        os.mkdir(dir)
    numbers = [int(i[:-4]) for i in os.listdir(dir) if i[:-4].isnumeric()]
    image_name = str((max(numbers) if numbers != [] else 0) + 1)
    image.draw_data(tab, dir, image_name)
    print(f"💾 Image saved under the name : {image_name}.png")


    
