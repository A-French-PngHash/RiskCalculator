from classes import Configuration
from proba_calc.proba_calc import RiskProbaCalculator
from image.image_draw_service import ImageDrawingService
import os
import sys

argument = sys.argv
dirName = os.path.dirname(os.path.abspath(__file__))


# Configuration
def config():
    nb_capitaux_at, nb_bombardiers_at, nb_chasseurs_at = tuple(list(map(int, input("🚀 Vaisseaux de l'attaquant 😈 (capitaux bombardier chasseur) : ").split(" "))))
    nb_capitaux_de, nb_bombardiers_de, nb_chasseurs_de = tuple(list(map(int, input("🚀  Vaisseaux du défenseur 🛡️ (capitaux bombardier chasseur) : ").split(" "))))
    
    attack_stop_condition = int(input("Enter the amount of soldier under which you do not want to continue the attack (minimum amount of soldier left): "))

    is_base_present = input("🏰 Is there an imperial base on the defender planet ? (y/n) : ").lower() == "y"
    death_star = input("⚡ Is there a death star on the defender planet ? (y/n) : ").lower() == "y"
    death_star_fight_bonus = 0
    if death_star:
        death_star_fight_bonus = int(input("Attack bonus (positive or negative) on the death star : "))
    
    
    configuration = Configuration(
        vaisseaux_att=[nb_capitaux_at, nb_bombardiers_at, nb_chasseurs_at],
        vaisseaux_def=[nb_capitaux_de, nb_bombardiers_de, nb_chasseurs_de], 
        base=is_base_present,
        death_star=death_star,
        death_star_fight_bonus=death_star_fight_bonus,
        attack_stop_condition=attack_stop_condition
        )
    return configuration


if __name__=="__main__":
    if "debug" in sys.argv:
        configuration = Configuration(
            vaisseaux_att=[2, 1, 0], 
            vaisseaux_def=[0, 0, 0], 
            base=False,
            death_star=True, 
            death_star_fight_bonus=0,
            attack_stop_condition=0)
        attack, defense = 10, 10
    else:
        configuration = config()
        attack, defense = tuple(list(map(int, input("Size of the table to generate (attack defense) : ").split(" "))))
    
    print("🏇 Calculating probabilities...")
    risk_prob = RiskProbaCalculator(configuration)
    prob_table = risk_prob.compute_all(attack, defense)
    print("🎨 Generating image...")
    image = ImageDrawingService()

    dir = f"{dirName}/output"
    if not os.path.exists(dir):
        os.mkdir(dir)
    numbers = [int(i[:-4]) for i in os.listdir(dir) if i[:-4].isnumeric()]
    image_name = str((max(numbers) if numbers != [] else 0) + 1)
    image.draw_data(tab=prob_table, finaldir=dir, finalname=image_name, use_gradient=True)
    print(f"💾 Image saved under the name : {image_name}.png")