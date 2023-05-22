class skeleton(Monster):
    abil = {"weapon": 6}
    def __init__(self, dmg):
        super.__init__("Skeleton", 10)
        self.abil["weapon"] = dmg
