class Character:
    Char = {'Name': "", 'Class': ""}
    StatsHp = {'Hp': 10, 'Mp': 10, 'MaxHp': 10, 'MaxMp': 10}
    Stats = {'Str': 0, 'Dex': 0, 'Con': 0, 'Wis': 0, 'Int': 0, 'Cha': 0, 'AC': 0, 'StrMod': 0, 'DexMod': 0, 'ConMod':0, 'WisMod': 0, 'IntMod':0, 'ChaMod': 0}
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
        self.Stats["DexMod"] = statList[8]
        self.Stats["ConMod"] = statList[9]
        self.Stats["WisMod"] = statList[10]
        self.Stats["IntMod"] = statList[11]
        self.Stats["ConMod"] = statList[12]
    def setMax(self, num):
        self.StatsHp["MaxHp"]
