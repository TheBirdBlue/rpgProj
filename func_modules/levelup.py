import common
import time
import saveload
import sys
sys.path.insert(1, './save')

file = 'save/savePassive.txt'

def levelUp(playerInfo):
    levelup = True
    passiveBonus = saveload.loadPassive(file)

    statChange = (playerInfo['playerHP'], playerInfo['playerSP'], playerInfo['playerAtk'],
                  playerInfo['playerDef'], playerInfo['playerMAtk'], playerInfo['playerMDef'], playerInfo['playerSpe'])
    statDisplay = ('HP', 'SP', 'Atk', 'Def', 'MAtk', 'MDef', 'Spe')
    editList = list(statChange)

    while levelup:
        levelCheck = 0
        statNum = 1
        print(' Pick ' + str(passiveBonus[8]) + ' stats to upgrade.')
        for display in statDisplay:
            print(' ' + str(statNum) + '  |  ' + display)
            statNum += 1

        choices = input(' Please input ' + str(passiveBonus[8]) + ' numbers: ')

        # Check input and add stats
        try:

            # Remove spaces
            if ' ' in choices:
                choices = choices.replace(' ', '')

            # Check if correct number of choices
            if len(choices) == passiveBonus[8]:

                checkCount = 0
                for value in choices:
                    value = int(value)

                    # Check and count input as valid
                    if value in range(1, 7):
                        checkCount += 1

                        # All three pass and stats are added
                        if checkCount == 3:

                            for value in choices:
                                value = int(value)

                                # Check values and add stats
                                if value == 1:
                                    editList[0] += 2
                                    levelCheck += 1

                                elif value == 2:
                                    editList[1] += 2
                                    levelCheck += 1

                                elif value == 3:
                                    editList[2] += 1
                                    levelCheck += 1

                                elif value == 4:
                                    editList[3] += 1
                                    levelCheck += 1

                                elif value == 5:
                                    editList[4] += 1
                                    levelCheck += 1

                                elif value == 6:
                                    editList[5] += 1
                                    levelCheck += 1

                                elif value == 7:
                                    editList[6] += 1
                                    levelCheck += 1

                            if levelCheck == 3:
                                playerInfo['playerLevel'] += 1
                                levelup = False

                    # When one input failed, end here and try again.
                    else:
                        print(' Invalid stat option.')
                        time.sleep(2)

            else:
                print(' Double check your number of choices.')
                print(' (Did you forget a passive bonus?)')
                time.sleep(2)


        except:
            print(' Something went wrong. Please try again.')

    common.clear()
    levelLine = ' {:5} : {} -> {}'
    print('')
    print(levelLine.format('Level', playerInfo['playerLevel'] - 1, playerInfo['playerLevel']))
    time.sleep(0.3)
    for name, currStat, display in zip(statDisplay, statChange, editList):
        print(levelLine.format(name, str(currStat), str(display)))
        time.sleep(0.3)

    input('\n Press enter to continue.')
    playerInfo['playerHP'] = editList[0]
    playerInfo['playerSP'] = editList[1]
    playerInfo['playerAtk'] = editList[2]
    playerInfo['playerDef'] = editList[3]
    playerInfo['playerMAtk'] = editList[4]
    playerInfo['playerMDef'] = editList[5]
    playerInfo['playerSpe'] = editList[6]
