from Character import Character
from Monsters import Monsters
from Skeleton import Skeleton
from Barbarian import Barbarian
from Druid import Druid
import random

def weapon(Monsters):
    print("spin a d20 for ac, you need to beat a " + "13" + " (Strength Modifier added to it)")
    input()
    roll = random.randint(1, 20)
    print(str(roll) + " + " + str(Hero.Stats["StrMod"]))
    if roll + Hero.Stats["StrMod"] >= Monsters.Stats["AC"]:
        print("Hit! roll for  Damage")
        input()
        rollD = random.randint(1, Hero.Abilities["weapon"])
        if Hero.Char["Class"] == "Barbarian":
            rollD += Hero.Stats["StrMod"]
        if roll + Hero.Stats["StrMod"] >= 20:
            print("Roll was crit, so double damage")
            rollD = rollD + rollD
        print("You did " + str(rollD) + " Damage")
        Monsters.Stats["Hp"] -= rollD
        print("Monster Hp is: " + str(Monsters.Stats["Hp"]))
    else:
        print("You failed to pierce the Monster's AC")
def transform(Monsters):
    print("You transform!")
    input()
    Hero.swapBear()
def rage(Monsters):
    print("With your Barbarian Rage, you gain HP!")
    print("You gain " + str(int(Hero.StatsHp["MaxHp"]/3)) + " HP!")
    Hero.StatsHp["Hp"] += int(Hero.StatsHp["MaxHp"]/3)
    if Hero.StatsHp["Hp"] > Hero.StatsHp["MaxHp"]:
        Hero.StatsHp["Hp"] = Hero.StatsHp["MaxHp"]
    print("Hp is now: " + str(Hero.StatsHp["Hp"]))

def punch(Monsters):
    if Hero.getBear() == True:
        print('Since you are a bear, you get a buff to your stats. Roll a D20 to see if you pierce ' + Monsters.Mons["Name"] + "'s armour.")
        input()
        rollTwen = random.randint(1, 20)
        print(str(rollTwen) + " + " + str(Hero.Stats["StrMod"] + 3))
        if rollTwen + Hero.Stats["StrMod"] + 3 >= Monsters.Stats["AC"]:
            print("Hit! roll for  Damage")
            input()
            rollD = random.randint(1, Hero.Abilities["punch"] + 4)
            rollD += Hero.Stats["WisMod"]
            if rollTwen + Hero.Stats["StrMod"] >= 20:
                print("Roll was crit, so double damage")
                rollD = rollD + rollD
            print("You did " + str(rollD) + " Damage")
            Monsters.Stats["Hp"] -= rollD
            print("Monster Hp is: " + str(Monsters.Stats["Hp"]))
        else:
            print("You failed to pierce the Monster's AC")
    else:
        print("You are not a bear and thus are weaker. Roll a D20 to see if you pierce " + Monster.Mons["Name"] + "'s armour")
        input()
        rollTwen = random.randint(1, 20)
        print(str(rollTwen) + " + " + str(Hero.Stats["StrMod"]))
        if rollTwen + Hero.Stats["StrMod"] + 3 >= Monsters.Stats["AC"]:
            print("Hit! roll for  Damage")
            input()
            rollD = random.randint(1, Hero.Abilities["punch"])
            rollD += Hero.Stats["WisMod"]
            if rollTwen + Hero.Stats["StrMod"] >= 20:
                print("Roll was crit, so double damage")
                rollD = rollD + rollD
            print("You did " + str(rollD) + " Damage")
            Monsters.Stats["Hp"] -= rollD
            print("Monster Hp is: " + str(Monsters.Stats["Hp"]))
        else:
            print("You failed to pierce the Monster's AC")
def battle(Monsters):
    print("Battle! Your enemy is " + Monsters.Mons["Name"] + " with " + str(Monsters.Stats["MaxHp"]) + " health!")
    monsterAlive = True
    while monsterAlive:
        print("Your move, " + Hero.Char["Name"])
        print(Hero.Abilities.keys())
        print("type the ability exactly of what you want to do")
        inputB = input().lower()

        if inputB == "weapon":
           weapon(Monsters)
        elif inputB == "rage":
            rage(Monsters)
        elif inputB == 'transform':
            transform(Monsters)
        elif inputB == 'punch':
            punch(Monsters)
        else:
            print("Nice spelling, bucko")
            continue
        if Monsters.Stats["Hp"] > 0:
            rollM = random.randint(1,20)
            print("***Monster Attacks***")
            print(rollM)
            if rollM + Monsters.Abil["Crit"] > Hero.Stats["AC"]:
                print("Hit!")
                rollMD = random.randint(1,6)
                print("Monster does " + str(rollMD) + " + " + str(Monsters.Abil["Crit"]) + " Damage")
                Hero.StatsHp["Hp"] -= rollMD + Monsters.Abil["Crit"]
                print("You went down to " + str(Hero.StatsHp["Hp"]) + " hp!")
                if Hero.StatsHp["Hp"] <= 0:
                    print("You lose!")
                    monsterAlive = False
            else:
                print("Monster does not pierce AC")
        else:
            monsterAlive = False
            print("You win the battle!")


print("Welcome to the dungeon!")
print("a: make character")
input1 = input().lower()
if input1 == "a":
    print("What is your name?")
    tempName = input()
    print("Choose a class:")
    print("a:Barbarian\nb:Druid\nc:Wizard")
    input2 = input()
    if input2 == "a":
        tempclass = "Barbarian"
    elif input2 == "b":
        tempclass = "Druid"
    elif input2 == "c":
        tempclass = "Wizard"
    else:
        print("Crashed")
    if tempclass == "Barbarian":
        Hero = Barbarian(tempclass, tempName)
        Hero.StatsHp["MaxHp"] = 16
        Hero.StatsHp["MaxMp"] = 8
        Hero.StatsHp["Mp"] = 8
        Hero.StatsHp["Hp"] = 16
    elif tempclass == "Druid":
        Hero = Druid(tempclass, tempName)
        Hero.StatsHp["MaxHp"] = 12
        Hero.StatsHp["MaxMp"] = 20
        Hero.StatsHp["Mp"] = 20
        Hero.StatsHp["Hp"] = 12
    print("The adventure begins!")

Skele = Skeleton(6)
battle(Skele)