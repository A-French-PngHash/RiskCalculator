class Configuration:
    vaisseaux_j1 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 1
    vaisseaux_j2 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 2
    base : bool # True si base impériale présente
    nb_troupes_j1 : int
    nb_troupes_j1 : int


class case:
    gagne : bool # True si le joueur 1 gagne
    nb_troupes_restantes : int

    def __init__(self, gagne, nb_troupes_restantes):
        self.gagne = gagne
        self.nb_troupes_restantes = nb_troupes_restantes
        



class tableau:
    vaisseaux_j1 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 1
    vaisseaux_j2 : list[int, int, int] # [nb_vaisseaux_capitaux, nb_bombardiers, nb_chasseurs] pour le joueur 2
    liste_proba : list[list[case]]

    def __init__(self, vaisseaux_j1, vaisseaux_j2, liste_proba):
        self.vaisseaux_j1 = vaisseaux_j1
        self.vaisseaux_j2 = vaisseaux_j2
        self.liste_proba = liste_proba


# case00 = case(True, 5)
# case01 = case(False, 2)
# case10 = case(True, 1)
# case11 = case(False, 3)

# tableau_proba = tableau([1, 0, 0], [2, 1, 0], [[case00, case01], [case10, case11]])