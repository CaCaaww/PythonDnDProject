class Character:
    Char = {'Name': "", 'Class': ""}
    StatsHp = {'Hp': 10, 'Mp': 10, 'MaxHp': 10, 'MaxMp': 10}
    Stats = {'Str': 0, 'Dex': 0, 'Con': 0, 'Wis': 0, 'Int': 0, 'Cha': 0, 'AC': 0, 'StrMod': 0}
    def __init__(self, _classT, _nameT):
        self.Char['Name'] = _nameT
        self.Char['Class'] = _classT
    def setStats(self, statList):
        self.Stats["Str"] = statList[0]
        self.Stats["Dex"] = statList[1]
        self.Stats["Con"] = statList[2]
        self.Stats["Wis"] = statList[3]
        self.Stats["Int"] = statList[4]
        self.Stats["Cha"] = statList[5]
        self.Stats["AC"] = statList[6]
        self.Stats["StrMod"] = statList[7]