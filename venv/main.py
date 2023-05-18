from Character import Character
import random
def battle(monster ):
    MonsterHP = 10
    print("Battle! Your enemy is " + monster + " with " + str(MonsterHP) + " health!")
    monsterAlive = True
    while monsterAlive:
        print("Your move, " + Hero.Char["Name"])
        print(Hero.Abilities.keys())
        print("give letter indicating ability. a = 1, b = 2, etc.")
        inputB = input().lower()
        if inputB == "a":
            print("spin a d20 for ac, you need to beat a " + "13" + " (Strength Modifier added to it)")
            input()
            roll = random.randint(1,20)
            print (str(roll)  + " + " + str(Hero.Stats["StrMod"]))
            if roll + Hero.Stats["StrMod"] >= 13:
                print("Hit! roll for  Damage")
                input()
                rollD = random.randint(1, Hero.Abilities["Weapon"]) + Hero.Stats["StrMod"]
                if roll + Hero.Stats["StrMod"] >= 20:
                    print("Roll was crit, so double damage")
                    rollD = rollD + rollD
                print("You did " + str(rollD) + " Damage")
                MonsterHP = MonsterHP - rollD
                print("Monster Hp is: " + str(MonsterHP))
            else:
                print("You failed to pierce the Monster's AC")
        if inputB == "b":
            print("With your Barbarian Rage, you gain HP!")
            print("You gain " + str(int(Hero.Abilities["Rage"])) + " HP!")
            Hero.StatsHp["Hp"] += int(Hero.Abilities["Rage"])
            if Hero.StatsHp["Hp"] > Hero.StatsHp["MaxHp"]:
                Hero.StatsHp["Hp"] = Hero.StatsHp["MaxHp"]
            print("Hp is now: " + str(Hero.StatsHp["Hp"]))
        if MonsterHP > 0:
            rollM = random.randint(1,20)
            print("***Monster Attacks***")
            print(rollM)
            if rollM + 1 > Hero.Stats["AC"]:
                print("Hit!")
                rollMD = random.randint(1,6)
                print("Monster does " + str(rollMD) + " Damage")
                Hero.StatsHp["Hp"] -= rollMD
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
    print("a:Barbarian\nb:Cleric\nc:Wizard")
    input2 = input()
    if input2 == "a":
        tempclass = "Barbarian"
    elif input2 == "b":
        tempclass = "Cleric"
    elif input2 == "c":
        tempclass = "Wizard"
    else:
        print("Crashed")
    Hero=Character(tempclass,tempName)
    print("The adventure begins!")
if Hero.Char.get('Class') == "Barbarian":
    Hero.StatsHp["Hp"] = 10 + 6
    Hero.StatsHp["Mp"] = 8
battle("Skeleton")