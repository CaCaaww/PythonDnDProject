from Character import Character
class Barbarian(Character):
    Abilities = {'weapon': 8, 'rage': 0}
    def __init__(self, classT, nameT):
        super().__init__(classT, nameT)
        self.setStats([17, 12, 16, 10, 10, 12, 13, 3, 1, 3, 0, 0, 1])

