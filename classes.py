class Configuration:
    vaisseaux_at : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour l'attaquant
    vaisseaux_de : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le défenseur
    base : bool # True si base impériale présente
    nb_troupes_at : int
    nb_troupes_de : int

    def __init__(self, vaisseaux_at, vaisseaux_de, base, nb_troupes_at, nb_troupes_de):
        self.vaisseaux_at = vaisseaux_at
        self.vaisseaux_de = vaisseaux_de
        self.base = base
        self.nb_troupes_at = nb_troupes_at
        self.nb_troupes_de = nb_troupes_de


class case:
    proba : float # probabilité que l'attaquant gagne
    nb_troupes_restantes : int # espérance des troupes restantes de l'attaquant

    def __init__(self, proba, nb_troupes_restantes):
        self.proba = proba
        self.nb_troupes_restantes = nb_troupes_restantes


class tableau:
    config : Configuration
    liste_proba : list[list[case]]

    def __init__(self, config, liste_proba):
        self.config = config
        self.liste_proba = liste_proba