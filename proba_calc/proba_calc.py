from math import floor
import numpy as np

import sys
import os

from utils import printProgressBar

dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{dirname}/../')

from classes import Configuration, Tableau, Case

class RiskProbaCalculator:
    configuration: Configuration
    computed_probabilities = {}

    def __init__(self,configuration : Configuration):
        self.configuration = configuration

    def _multiply_special(self,input:list[list[int]]):
        """
        Input : 
        [[4, 1],
            [3, 4]
            [7], ]
        output : 
        [[4, 3, 7], [4, 4, 7], [1, 3, 7], [1, 4, 7]]
        """
        return np.array(np.meshgrid(*input)).T.reshape(-1, len(input))


    def _compute_battle(self, attack: int, defense:int, death_defeated = False) -> float:
        """
        Returns the probability for the attack to win and the number of soldier left in attack (if attack wins) and in defense (if defense wins).
        """
        if (defense == 0):
            return 1
        if (attack == 0):
            return 0
        
        death_star_to_fight = self.configuration.death_star and not death_defeated

        if (attack, defense, death_star_to_fight) in self.computed_probabilities:
            return self.computed_probabilities[(attack, defense, death_star_to_fight)]
        
        # 5 case : 
        # attack loses 2 soldier
        # attack and defense lose 1 soldier
        # defense lose 2 soldier
        # attack loses 1 soldier
        # defense lose 1 soldier

        # For each case, compute the probability and then call recursively.
        def_pwr = min(defense, 2)
        att_pwr = min(attack, 3)

        att_cap = self.configuration.vaisseaux_att[0]
        def_cap = self.configuration.vaisseaux_def[0]

        att_chasseur = self.configuration.vaisseaux_att[2]
        def_chasseur = self.configuration.vaisseaux_def[2]
        

        defense_liste = [[i for i in range(2 if (def_chasseur > dice) else 1 , 9 if (self.configuration.base or def_cap > dice) else 7)] for dice in range(def_pwr)]
        attaque_liste = [[i for i in range(2 if (att_chasseur > dice) else 1, 9 if (att_cap > dice) else 7)] for dice in range(att_pwr)]
        

        def_dice = self._multiply_special(defense_liste)
        att_dice = self._multiply_special(attaque_liste)

        if death_star_to_fight:
            possibilities = len(att_dice)
            defeat_death_star = 0
            destroyed_by_death_star = 0
            for i in att_dice:
                if sum(i) + self.configuration.death_star_fight_bonus < 18:
                    destroyed_by_death_star += 1
                else:
                    defeat_death_star += 1
            result = (defeat_death_star * self._compute_battle(attack, defense, death_defeated=True) +
                    destroyed_by_death_star * self._compute_battle(max(attack - 3, 0), defense, death_defeated=False)
            )/possibilities
            self.computed_probabilities[(attack, defense, death_star_to_fight)] = result
            return result

        possibilities = len(def_dice) * len(att_dice)
        proba = 0
        soldier_left_att = 0
        soldier_left_def = 0
        if def_pwr == 1 or att_pwr == 1:
            def_lose_one = 0
            att_lose_one = 0
            for att in att_dice:
                for deff in def_dice:
                    max_att = max(att) + (1 if self.configuration.vaisseaux_att[1] >= 1 else 0)
                    max_def = max(deff) + (1 if self.configuration.vaisseaux_def[1] >= 1 else 0)

                    if max_att > max_def:
                        def_lose_one += 1
                    else:
                        att_lose_one += 1
            proba = (def_lose_one * self._compute_battle(attack=attack, defense=defense - 1) 
                     + att_lose_one * self._compute_battle(attack=attack - 1, defense=defense))/possibilities
        
        else:
            att_lose_two = 0
            def_lose_two = 0
            one_each = 0

            for att in att_dice:
                for deff in def_dice:
                    satt = sorted(att, reverse=True)
                    sdeff = sorted(deff, reverse=True)

                    att_bomb = self.configuration.vaisseaux_att[1]
                    def_bomb = self.configuration.vaisseaux_def[1]

                    a1, a2 = satt[0], satt[1]
                    d1, d2 = sdeff[0], sdeff[1]

                    if att_bomb >= 1:
                        a1 += 1
                    if att_bomb >= 2:
                        a2 += 1
                    if def_bomb >= 1:
                        d1 += 1
                    if def_bomb >= 2:
                        d2 += 1


                    if a1 > d1 and a2 > d2:
                        def_lose_two +=1
                    elif a1 <= d1 and a2 <= d2:
                        att_lose_two += 1
                    else:
                        one_each += 1

            proba = (att_lose_two * self._compute_battle(attack - 2, defense)
                    + def_lose_two * self._compute_battle(attack, defense - 2)
                    + one_each * self._compute_battle(attack - 1, defense - 1))/possibilities
        self.computed_probabilities[(attack, defense)] = proba
        return proba
    
    def compute_battle(self,attack : int, defense : int, reset : bool = True):
        """
        Computes the probabilities for the attack to win. The reset option resets the `computed_probabilities` dictionary.
        """
        if reset:
            print("Resetting")
            self.computed_probabilities = {}
        return self._compute_battle(attack, defense)

    def compute_all(self, attack: int, defense:int) -> Tableau:
        """
        Computes all the value from the (attack, defense) point
        """
        self.computed_probabilities = {}
        cases = []
        total_count = attack * defense
        for i in range(1, attack + 1):
            line = []
            for j in range(1, defense + 1):
                line.append(Case(self.compute_battle(i, j, False), 0))
                printProgressBar((i-1) * defense + j, total_count)
            cases.append(line)
            percentage = floor(i * defense/total_count * 1000)/10
        return Tableau(self.configuration, cases)
    
