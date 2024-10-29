class Configuration:
    vaisseaux_j1 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 1
    vaisseaux_j2 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 2
    base : bool # True si base impériale présente
    nb_troupes_j1 : int
    nb_troupes_j2 : int

    def __init__(self, vaisseaux_j1, vaisseaux_j2, base, nb_troupes_j1, nb_troupes_j2):
        self.vaisseaux_j1 = vaisseaux_j1
        self.vaisseaux_j2 = vaisseaux_j2
        self.base = base
        self.nb_troupes_j1 = nb_troupes_j1
        self.nb_troupes_j2 = nb_troupes_j2


class case:
    proba : float # probabilité que le joueur 1 gagne
    nb_troupes_restantes : int # espérance des troupes restantes du joueur 1

    def __init__(self, proba, nb_troupes_restantes):
        self.proba = proba
        self.nb_troupes_restantes = nb_troupes_restantes


class tableau:
    config : Configuration
    liste_proba : list[list[case]]

    def __init__(self, configuration, liste_proba):
        self.configuration = configuration
        self.liste_proba = liste_proba