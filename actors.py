import random


class Hero(object):
    """docstring for Hero"""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        print(f"Our hero {self.name} attacks {opponent.name}!")

        hero_roll = random.randint(1, 12) * self.level
        opp_roll = random.randint(1, 12) * opponent.level

        print(f"You roll {hero_roll}..."
        print(f"The {opponent.name} rolls {opp_roll}...")

        if hero_roll >= opp_roll:
            print(f"{self.name} has remained victorious over {opponent.name}!\n")
            return True
        else:
            print(f"DEFEAT! {opponent.name} has overpowered {self.name}!\n")
            return False


class Opponent(object):
    """docstring for Opponent"""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"Digital Oppononent: {self.name} at Level {self.level}"

# class SmallOpponent(Opponent):
#     """docstring for SmallOpponent"""
#     def __init__(self, arg):
#         super(Opponent, self).__init__()
#         self.arg = arg
