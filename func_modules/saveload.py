
def createOver(file, charLvl, charExp, charMun, charHP, charSP, charAtk, charDef, charMAtk, charMDef, charSpe, rebirth):
    loadOrder = [1, 0, 0, 10, 10, 5, 5, 5, 5, 5, 0]
    with open(file, 'a+') as save:

        # Overworld Info
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')

        # Stat Info
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')
        save.write(str(loadOrder[7]) + '\n')
        save.write(str(loadOrder[8]) + '\n')
        save.write(str(loadOrder[9]) + '\n')
        save.write(str(loadOrder[10]) + '\n')

    return loadOrder

def createSkill(file):
    # Skill format
    # NAME, P(hysical) or M(agical), SP COST, POWER, ELEMENT, SPECIAL
    firstSkill = 'Attack,p,0,1.5,none,0'
    with open(file, 'a+') as save:
        save.write(firstSkill)

def createPassive(file):
    # Formatted for permanent boosts and bonuses
    # LEVEL CAP, HP, SP, ATK, DEF, MATK, MDEF, SPD, ABILITY POINTS
    loadOrder = [20, 0, 0, 0, 0, 0, 0, 0, 3]
    with open(file, 'a+') as save:
        save.write(str(loadOrder[0]) + '\n')
        save.write(str(loadOrder[1]) + '\n')
        save.write(str(loadOrder[2]) + '\n')
        save.write(str(loadOrder[3]) + '\n')
        save.write(str(loadOrder[4]) + '\n')
        save.write(str(loadOrder[5]) + '\n')
        save.write(str(loadOrder[6]) + '\n')
        save.write(str(loadOrder[7]) + '\n')
        save.write(str(loadOrder[8]) + '\n')

    return loadOrder

def save(file, charList):
    saveOrder = [charList[0], charList[1], charList[2], charList[3], charList[4], charList[5], charList[6],
                 charList[7], charList[8], charList[9], charList[10]]
    with open(file, 'w') as save:
        for line in saveOrder:
            str(line).rstrip('\n')
            save.write(str(line))
            save.write('\n')

def loadOver(file, loadList):
    loadOrder = []
    with open(file, 'r') as save:
        for line in save:
            line = line.replace('\n', '')
            line = int(line)
            loadOrder.append(line)

    return loadOrder

def loadPassive(file):
    loadOrder = []
    with open(file, 'r') as save:
        for line in save:
            line = line.replace('\n', '')
            line = int(line)
            loadOrder.append(line)

    return loadOrder

def restart(playerFile, playerPassive, playerSkills):
    pass
