class Configuration:
    vaisseaux_att : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 1
    vaisseaux_def : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 2
    base : bool # True si base impériale présente
    death_star : bool
    death_star_fight_bonus: int # The bonus (or malus if negative) given by the force index.
    attack_stop_condition: int # Stop when this amount of soldier is left for the attack.

    def __init__(self, vaisseaux_att, vaisseaux_def, base, death_star, death_star_fight_bonus, attack_stop_condition):
        self.vaisseaux_att = vaisseaux_att
        self.vaisseaux_def = vaisseaux_def
        self.base = base
        self.death_star = death_star
        self.death_star_fight_bonus = death_star_fight_bonus
        self.attack_stop_condition = attack_stop_condition

    def __repr__(self) -> str:
        return str(self.vaisseaux_att) + " " + str(self.vaisseaux_def) + " Base : " + ("oui" if self.base else "non") + " Etoile noire : "+ ("oui" if self.death_star else "non")


class Case:
    proba : float # probabilité que le joueur 1 gagne
    nb_troupes_restantes : float # espérance des troupes restantes du joueur 1

    def __init__(self, proba, nb_troupes_restantes):
        self.proba = proba
        self.nb_troupes_restantes = nb_troupes_restantes

    def __str__(self) -> str:
        return str(self.proba)
    
    def __repr__(self) -> str:
        return str(self.proba)


class Tableau:
    config : Configuration
    liste_proba : list[list[Case]]

    def __init__(self, config, liste_proba):
        self.config = config
        self.liste_proba = liste_proba

    def __repr__(self):
        return "Configuration : " + str(self.config) + "\n" + "Probabilités : " + str(self.liste_proba)