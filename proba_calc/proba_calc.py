import numpy as np

import sys
sys.path.append('../')

from classes import Configuration

config = Configuration([1, 0, 0],[0, 0, 0], True, 10, 6)
computed_probabilities = {}

class AttackResult:
    attackWon: bool
    soldierLeft: int

    def __init__(self, attackWon, soldierLeft) -> None:
        self.attackWon = attackWon
        self.soldierLeft = soldierLeft

def multiply_special(input:list[list[int]]):
    """
    Input : 
    [
        [4, 1],
        [3, 4]
        [7],
    ]

    output : 
    [[4, 3, 7], [4, 4, 7], [1, 3, 7], [1, 4, 7]]
    """

    return np.array(np.meshgrid(*input)).T.reshape(-1, len(input))


def compute_battle(attack: int, defense:int, configuration : Configuration) -> float:
    """
    Returns the probability for the attack to win and the number of soldier left in attack (if attack wins) and in defense (if defense wins).
    """
    if (defense == 0):
        return 1
    if (attack == 0):
        return 0
    if (attack, defense) in computed_probabilities:
        return computed_probabilities[(attack, defense)]
    
    # 5 case : 
    # attack loses 2 soldier
    # attack and defense lose 1 soldier
    # defense lose 2 soldier
    # attack loses 1 soldier
    # defense lose 1 soldier

    # For each case, compute the probability and then call recursively.
    def_pwr = min(defense, 2)
    att_pwr = min(attack, 3)

    att_cap = configuration.vaisseaux_att[0]
    def_cap = configuration.vaisseaux_def[0]
    

    defense_liste = [[i for i in range(1, 9 if (configuration.base or def_cap > dice) else 7)] for dice in range(def_pwr)]
    attaque_liste = [[i for i in range(1, 9 if (att_cap > dice) else 7)] for dice in range(att_pwr)]
    
    def_dice = multiply_special(defense_liste)
    att_dice = multiply_special(attaque_liste)


    possibilities = len(def_dice) * len(att_dice)
    proba = 0
    soldier_left_att = 0
    soldier_left_def = 0
    if def_pwr == 1 or att_pwr == 1:
        def_lose_one = 0
        att_lose_one = 0
        for att in att_dice:
            for deff in def_dice:
                if max(att) > max(deff):
                    def_lose_one += 1
                else:
                    att_lose_one += 1
        proba = (def_lose_one * compute_battle(attack=attack, defense=defense - 1) + att_lose_one * compute_battle(attack=attack - 1, defense=defense))/possibilities
       
    else:
        att_lose_two = 0
        def_lose_two = 0
        one_each = 0

        for att in att_dice:
            for deff in def_dice:
                satt = sorted(att, reverse=True)
                sdeff = sorted(deff, reverse=True)
                a1, a2 = satt[0], satt[1]
                d1, d2 = sdeff[0], sdeff[1]
                if a1 > d1 and a2 > d2:
                    def_lose_two +=1
                elif a1 <= d1 and a2 <= d2:
                    att_lose_two += 1
                else:
                    one_each += 1

        proba = (att_lose_two * compute_battle(attack - 2, defense)
                  + def_lose_two * compute_battle(attack, defense - 2)
                  + one_each * compute_battle(attack - 1, defense - 1))/possibilities
        
        
    computed_probabilities[(attack, defense)] = proba

    return proba

print(compute_battle(5, 1))
#print(computed_probabilities)