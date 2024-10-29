# Computing : 

from classes import Tableau, Configuration
from proba_calc.proba_calc import RiskProbaCalculator
from pilo.pilo import ImageDrawingService


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
    configuration = config()
    risk_prob = RiskProbaCalculator(configuration)
    list_prob = risk_prob.compute_all(10, 10)
    tab = Tableau(configuration,list_prob)
    image = ImageDrawingService()
    image.draw_data(tab, "tqet", "test")


    


# configuration = Configuration([1, 0, 3],[0, 0, 0], False)
# risk_prob = RiskProbaCalculator(configuration)
# print(risk_prob.compute_all(10, 10))

