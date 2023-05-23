class Monsters:
    Mons = {"Name": ""}
    Stats = {"MaxHp": 20, "Hp": 20, "AC": 10}
    Abil = {"Crit": 0}
    def __init__(self, nameT, maxHP):
        self.Mons["Name"] = nameT
        self.Stats["MaxHp"] = maxHP
        self.Stats["Hp"] = maxHP

    def setCrit(self, num):
        self.Abil["Crit"] = num
    def setAC(self, num):
        self.Stats["AC"] = num