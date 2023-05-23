from Monsters import Monsters
class Skeleton(Monsters):
    abil = {"weapon": 6}
    def __init__(self, dmg):
        super().__init__( "Skeleton", 10)
        self.abil["weapon"] = dmg
        self.setCrit(2)
        self.setAC(13)
