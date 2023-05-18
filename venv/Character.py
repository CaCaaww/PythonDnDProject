class Character:
    Char = {'Name': "", 'Class': ""}
    StatsHp = {'Hp': 10, 'Mp': 10, 'MaxHp': 10, 'MaxMp': 10}
    Abilities = {'Weapon': 8, 'Rage': int(StatsHp.get('MaxHp')/3)}
    Stats = {'Str': 17, 'Dex': 12, 'Con': 16, 'Wis': 10, 'Int': 10, 'Cha': 12, 'AC': 16, 'StrMod': 4}
    def __init__(self, _classT, _nameT):
        self.Char['Name'] = _nameT
        self.Char['Class'] = _classT

