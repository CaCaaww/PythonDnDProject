from Character import Character
class Druid(Character):
    IsBear = False
    Abilities = {"punch": 6, "transform": 0}
    def __init__(self, classT, nameT):
        super().__init__(classT, nameT)
        self.setStats([11, 13, 16, 15, 15, 14, 11, 0, 1, 3, 2, 2, 2])
    def getBear(self):
        return self.IsBear
    def swapBear(self):
        if self.IsBear == True:
            self.IsBear = False

        else:
            self.IsBear = True