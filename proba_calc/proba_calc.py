class AttackResult:
    attackWon: bool
    soldierLeft: int

    def __init__(self, attackWon, soldierLeft) -> None:
        self.attackWon = attackWon
        self.soldierLeft = soldierLeft


def compute_battle(attack: int, defense:int) -> (float):
    """
    Returns the probability for the attack to win.
    """
    if (defense == 0):
        return 1
    if (attack == 0):
        return 0
    
    # 5 case : 
    # attack loses 2 soldier
    # attack and defense lose 1 soldier
    # defense lose 2 soldier
    # attack loses 1 soldier
    # defense lose 1 soldier

    # For each case, compute the probability and then call recursively.
    if (defense) == 1 or (attack) == 1:
        def_pwr = min(defense, 2)
        att_pwr = min(attack, 3)
        def_number = []

