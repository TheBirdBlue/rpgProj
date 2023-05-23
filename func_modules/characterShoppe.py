import time
import common
import saveload
from playerSkills import playerSkillsDict

fileLocationUser = 'save/saveOverview.txt'
fileLocationSkills = 'save/saveSkills.txt'
fileLocationPassive = 'save/savePassive.txt'

basicList = ['HP   +5', 'SP   +5', 'Atk  +1', 'Def  +1', 'MAtk +1', 'MDef +1', 'Spe  +1', 'Exp  +10', 'Cancel']
rebirthList = ['Level Cap +10', 'HP +10', 'SP +10', 'Atk +1', 'Def +1', 'MAtk +1', 'MDef +1', 'Spe +1',
               'Ability Point + 1', 'Skills', 'Cancel']
shopSubMenu = ['Basic Upgrades', 'Premium Upgrades', 'Leave Shop']

def shoppeKeep(playerStats, playerPassive):

    shopOverview = True

    while shopOverview:

        # Initialize and name variables
        charLvl = playerStats[0]
        charExp = playerStats[1]
        charMun = playerStats[2]
        charHP = playerStats[3]
        charSP = playerStats[4]
        charAtk = playerStats[5]
        charDef = playerStats[6]
        charMAtk = playerStats[7]
        charMDef = playerStats[8]
        charSpe = playerStats[9]
        charRebirth = playerStats[10]
        charMaxLevel = playerPassive[0]

        playerList = [charLvl, charExp, charMun, charHP, charSP, charAtk, charDef, charMAtk, charMDef, charSpe,
                      charRebirth]

        # Print general overview
        common.clear()

        # Set line formats
        infoLineChar = ' ║ Lvl:{:>3} / {:<3} ║ Mun:{:>8} ║'
        infoLineExp = ' ║ Exp:{:>24} ║'
        expAmount = int(((charExp / 100)) * 21)
        expBar = ' [' + (' ' * (20 - expAmount)) + ('▓' * expAmount) + ']'
        charMunFormat = common.numConversion(charMun)
        choiceBar = ' ║ {:2} ║ {:<23} ║'

        choiceNum = 1

        # Print lines
        print(' ╔═══════════════╦══════════════╗')
        print(infoLineChar.format(charLvl, charMaxLevel, charMunFormat))
        print(' ╠═══════════════╩══════════════╣')
        print(infoLineExp.format(expBar))
        print(' ╠══════════════════════════════╣')
        print(' ║ The shop keeper greets you;  ║\n'
              ' ║ "Welcome. Come see my wares. ║')
        print(' ╠══════════════════════════════╣')
        for options in shopSubMenu:
            print(choiceBar.format(choiceNum, options))
            choiceNum += 1
        print(' ╚══════════════════════════════╝')

        playerInput = input(' Which would you like? ')

        #try:
        playerInput = int(playerInput)
        if playerInput in range(0, len(shopSubMenu) + 1):

            if playerInput == 1:
                playerStats = basicShop(playerList, charMaxLevel)

            elif playerInput == 2:
                playerStats, maxLvl = advanceShop(playerList, playerPassive)

            elif playerInput == 3:
                print('\n Good luck out there.')
                time.sleep(2)
                shopOverview = False
                saveload.save(fileLocationUser, playerStats)
                return playerStats

        else:
            print(' Sorry, that is not an option. -83')

        #except:
            print(' Sorry, that is not an option. -86')
            time.sleep(2)

def basicShop(playerList, maxLevel):

    shopBasic = True

    # Initialize and name variables
    charLvl = playerList[0]
    charExp = playerList[1]
    charMun = playerList[2]
    charHP = playerList[3]
    charSP = playerList[4]
    charAtk = playerList[5]
    charDef = playerList[6]
    charMAtk = playerList[7]
    charMDef = playerList[8]
    charSpe = playerList[9]
    charRebirth = playerList[10]
    charMaxLevel = maxLevel

    while shopBasic:

        playerList = [charLvl, charExp, charMun, charHP, charSP, charAtk, charDef, charMAtk, charMDef, charSpe,
                      charRebirth]

        statList = [int(charHP / 5), int(charSP / 5), charAtk, charDef, charMAtk, charMDef, charSpe]
        costList = []

        # Generate stat upgrade costs
        for stat in statList:
            cost = (stat + 1) * 7
            costList.append(cost)

        expCost = charLvl * 100
        costList.append(expCost)

        # Print general overview
        common.clear()

        # Set line formats
        infoLineChar = ' ║ Lvl:{:>3} / {:<3} ║ Mun:{:>9} ║'
        infoLineExp = ' ║ Exp:{:>25} ║'
        expAmount = int(((charExp / 100)) * 21)
        expBar = ' [' + (' ' * (21 - expAmount)) + ('▓' * expAmount) + ']'
        charMunFormat = common.numConversion(charMun)
        choiceBar = ' ║ {:2} ║ {:<24} ║ Cost: {:>6} ║'

        choiceNum = 1

        # Print lines
        print(' ╔═══════════════╦═══════════════╗')
        print(infoLineChar.format(charLvl, charMaxLevel, charMunFormat))
        print(' ╠═══════════════╩═══════════════╣')
        print(infoLineExp.format(expBar))
        print(' ╠═══════════════════════════════╣')
        print(' ║ "Ah yes, all muns spend the   ║\n'
              ' ║ same. What would you like?"   ║')
        print(' ╠═══════════════════════════════╬══════════════╗')
        for options, cost in zip(basicList, costList):
            print(choiceBar.format(choiceNum, options, cost))
            choiceNum += 1
        print(' ║  9 ║ Cancel                   ║              ║')
        print(' ╚═══════════════════════════════╩══════════════╝')

        playerInput = input(' Which would you like? ')
        try:
            playerInput = int(playerInput)
            if playerInput in range(1, len(basicList) + 1):

                if playerInput == 1:
                    if charMun >= costList[0]:
                        charMun -= costList[0]
                        charHP += 5
                        print(' HP increased by 5!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 2:
                    if charMun >= costList[1]:
                        charMun -= costList[1]
                        charSP += 5
                        print(' SP increased by 5!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 3:
                    if charMun >= costList[2]:
                        charMun -= costList[2]
                        charAtk += 1
                        print(' Attack increased by 1!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 4:
                    if charMun >= costList[3]:
                        charMun -= costList[3]
                        charDef += 1
                        print(' Defense increased by 1!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 5:
                    if charMun >= costList[4]:
                        charMun -= costList[4]
                        charMAtk += 1
                        print(' Magic Attack increased by 1!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 6:
                    if charMun >= costList[5]:
                        charMun -= costList[5]
                        charMDef += 1
                        print(' Magic Defense increased by 1!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                elif playerInput == 7:
                    if charMun >= costList[6]:
                        charMun -= costList[6]
                        charSpe += 1
                        print(' Special increased by 1!')
                        time.sleep(2)
                    else:
                        print(' Not enough muns for that.')
                        time.sleep(2)

                if playerInput == 8:
                    if charLvl == charMaxLevel:
                        print(' You seem to have reached your full potential.')
                        time.sleep(0.3)
                        print(' I cannot help you progress any further.')
                        time.sleep(2)
                    else:
                        cost = charLvl * 100
                        print(' Gained 10 experience!')
                        time.sleep(2)

                elif playerInput == 9:
                    print('\n I hope something caught your eye.')
                    time.sleep(2)
                    shopBasic = False
                    return playerList

            else:
                print(' Sorry, that is not an option. -227')

        except:
            print(' Sorry, that is not an option. -230')
            time.sleep(2)

def advanceShop(playerList, playerPassive):

    shopAdvance = True

    # Initialize and name variables
    charLvl = playerList[0]
    charExp = playerList[1]
    charMun = playerList[2]
    charHP = playerList[3]
    charSP = playerList[4]
    charAtk = playerList[5]
    charDef = playerList[6]
    charMAtk = playerList[7]
    charMDef = playerList[8]
    charSpe = playerList[9]
    charRebirth = playerList[10]
    charMaxLevel = playerPassive[0]

    costList = [100, 25, 25, 10, 10, 10, 10, 10, 900, '---']

    while shopAdvance:

        playerList = [charLvl, charExp, charMun, charHP, charSP, charAtk, charDef, charMAtk, charMDef, charSpe,
                      charRebirth]

        # Print general overview
        common.clear()

        # Set line formats
        infoLineChar = ' ║ Lvl:{:>3} / {:<3} ║ RBP:{:>9} ║'
        infoLineExp = ' ║ Exp:{:>25} ║'
        expAmount = int(((charExp / 100)) * 21)
        expBar = ' [' + (' ' * (21 - expAmount)) + ('▓' * expAmount) + ']'
        charRBRFormat = common.numConversion(charRebirth)
        choiceBar = ' ║ {:2} ║ {:<24} ║ Cost: {:>3} ║'

        choiceNum = 1

        # Print lines
        print(' ╔═══════════════╦═══════════════╗')
        print(infoLineChar.format(charLvl, charMaxLevel, charRBRFormat))
        print(' ╠═══════════════╩═══════════════╣')
        print(infoLineExp.format(expBar))
        print(' ╠═══════════════════════════════╣')
        print(' ║ "Ah yes, all muns spend the   ║\n'
              ' ║ same. What would you like?"   ║')
        print(' ╠═══════════════════════════════╬═══════════╗')
        for options, cost in zip(rebirthList, costList):
            print(choiceBar.format(choiceNum, options, cost))
            choiceNum += 1
        print(' ║ 11 ║ Cancel                   ║           ║')
        print(' ╚═══════════════════════════════╩═══════════╝')

        playerInput = input(' Which would you like? ')
        #try:
        playerInput = int(playerInput)
        if playerInput in range(1, len(rebirthList) + 1):

            if playerInput == 1:
                if charRebirth >= costList[0]:
                    playerPassive[0] += 10
                    charRebirth -= costList[0]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 2:
                if charRebirth >= costList[1]:
                    playerPassive[1] += 10
                    charRebirth -= costList[1]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 3:
                if charRebirth >= costList[2]:
                    playerPassive[2] += 1
                    charRebirth -= costList[2]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 4:
                if charRebirth >= costList[3]:
                    playerPassive[3] += 1
                    charRebirth -= costList[3]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 5:
                if charRebirth >= costList[4]:
                    playerPassive[4] += 1
                    charRebirth -= costList[4]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 6:
                if charRebirth >= costList[5]:
                    playerPassive[5] += 1
                    charRebirth -= costList[5]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 7:
                if charRebirth >= costList[6]:
                    playerPassive[6] += 1
                    charRebirth -= costList[6]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 8:
                if charRebirth >= costList[7]:
                    playerPassive[7] += 1
                    charRebirth -= costList[7]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 9:
                if charRebirth >= costList[8]:
                    playerPassive[8] += 1
                    charRebirth -= costList[8]
                else:
                    print(' You need to rebirth before you can afford this.')
                    time.sleep(2)

            elif playerInput == 10:
                charRebirth = skillShope(charRebirth)
                time.sleep(2)

            elif playerInput == 11:
                print('\n I hope something caught your eye.')
                time.sleep(2)
                shopAdvance = False
                return playerList, playerPassive

        else:
            print(' Sorry, that is not an option. -375')

        #except:
            #print(' Sorry, that is not an option. -378')
            #time.sleep(2)

def skillShope(rebirth):
    skill = True
    # Load current player skills
    playerPassive = []
    with open(fileLocationPassive, 'r') as skills:
        for line in skills:
            line = line.replace('\n', '')
            line = line.split(',')
            playerPassive.append(line)

    # First, build player actions
    playerActions = []
    with open(fileLocationSkills, 'r') as playerSkills:
        for line in playerSkills:
            line = line.replace('\n', '')
            line = line.split(',')
            playerActions.append(line)

    # Create the skill dict
    optionsDict = {}
    for skill, data in playerSkillsDict.items():
        for skillInfo in playerActions:
            if skillInfo[0] == skill:
                pass
            else:
                optionsDict[skill] = data

    # Forth, set up formatting and ready print lines

    while skill:

        print(' ╔═══════════════════╗')
        rbLine = ' ║ Rebirth: {:8} ║'
        print(rbLine.format(rebirth))
        print(' ╠════╦══════════════╬════════════════╦═════════╦═══════════╦═══════════════════╦═══════════════╗')
        skillLineFormat = ' ║ {:2} ║ {:12} ║ Type: {:>8} ║ SP: {:>3} ║ Pow: {:>4} ║ Element: {:>8} ║ RB Cost: {:4} ║'
        option = 1
        pullDatalist = []
        for skill, data in optionsDict.items():
            name = data['displayName']
            if data['type'] == 'p':
                type = 'Physical'
            elif data['type'] == 'm':
                type = 'Magical'
            elif data['type'] == 'e':
                type = 'Effect'
            else:
                type = ''
            spCost = data['spCost']
            power = data['power']
            element = data['element']
            element = element.capitalize()
            rbCost = data['rbCost']

            setupList = []
            for skillData in data.values():
                setupList.append(skillData)

            pullDatalist.append(setupList)

            print(skillLineFormat.format(str(option), name, type, spCost, power, element, rbCost))
            option += 1

        cancel = ' ║ {:<2} ║ Cancel       ║                ║         ║           ║                   ║               ║'
        print(cancel.format(option))
        print(' ╚════╩══════════════╩════════════════╩═════════╩═══════════╩═══════════════════╩═══════════════╝')

        skillshopinput = input(' What skill would you like to learn? ')

        try:
            skillshopinput = int(skillshopinput)

            # Check player input against list
            if skillshopinput in range(1, len(optionsDict) + 2):
                skillshopinput -= 1
                if skillshopinput == (len(optionsDict)):
                    skill = False
                    break

                else:
                    # Set skill into and format to be amended to skills
                    skilltolearn = pullDatalist[skillshopinput]
                    format = '\n' + str(skilltolearn[0]) + ',' + str(skilltolearn[1]) + ',' + str(skilltolearn[2]) + ',' +\
                             str(skilltolearn[3]) + ',' + str(skilltolearn[4]) + ',' + str(skilltolearn[5])

                    # Check for Rebirth Points

                    if rebirth >= skilltolearn[-1]:
                        rebirth -= skilltolearn[-1]
                        with open(fileLocationSkills, 'a+') as skillfile:
                            skillfile.write(format)

                        print(' You have learned ' + skilltolearn[0] + '!')
                        time.sleep(2)

                        skill= False
                        break

                    else:
                        print(' Not enough Rebirth Points.')
                        time.sleep(1)

            else:
                print(' Invalid choice.')
                time.sleep(2)

        except:
            print(' Invalid choice.')
            time.sleep(2)

    return rebirth
