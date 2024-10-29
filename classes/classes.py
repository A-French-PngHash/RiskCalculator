class case:
    gagne : bool # True si le joueur 1 gagne
    nb_troupes_restantes : int

    def __init__(self, gagne, nb_troupes_restantes):
        self.gagne = gagne
        self.nb_troupes_restantes = nb_troupes_restantes
        



class tableau:
    nb_vaisseaux_capitaux_j1 : int
    nb_vaisseaux_capitaux_j2 : int
    nb_chasseurs_j1 : int
    nb_chasseurs_j2 : int
    nb_bombardiers_j1 : int
    nb_bombardiers_j2 : int
    liste_proba : list[list[case]]

    def __init__(self, nb_vaisseaux_capitaux_j1, nb_chasseurs_j1, nb_bombardiers_j1, nb_vaisseaux_capitaux_j2, nb_chasseurs_j2, nb_bombardiers_j2, liste_proba):
        self.nb_vaisseaux_capitaux_j1 = nb_vaisseaux_capitaux_j1
        self.nb_chasseurs_j1 = nb_chasseurs_j1
        self.nb_bombardiers_j1 = nb_bombardiers_j1
        self.nb_vaisseaux_capitaux_j2 = nb_vaisseaux_capitaux_j2
        self.nb_chasseurs_j2 = nb_chasseurs_j2
        self.nb_bombardiers_j2 = nb_bombardiers_j2
        self.liste_proba = liste_proba


# case00 = case(True, 5)
# case01 = case(False, 2)
# case10 = case(True, 1)
# case11 = case(False, 3)

# tableau_proba = tableau(1, 0, 0, 2, 1, 0, [[case00, case01], [case10, case11]])