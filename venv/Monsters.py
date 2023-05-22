class Monsters:
    Mons = {"Name": ""}
    Stats = {"MaxHp": 20, "Hp": 20}

    def __init__(self, nameT, maxHP):
        self.Mons["Name"] = nameT
        self.Stats["MaxHp"] = maxHP
        self.Stats["Hp"] = maxHP
