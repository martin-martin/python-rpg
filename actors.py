



class Hero(object):
    """docstring for Wizard"""
    def __init__(self, name, level):
        self.name = name
        self.level = level

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
