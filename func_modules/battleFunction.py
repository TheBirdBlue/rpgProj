import levelup
import time
import saveload
import random
import common
from enemySkills import enemySkillsDict
from enemyDict import enemyInfoDict

playerFile = 'save/saveOverview.txt'
playerSkills = 'save/saveSkills.txt'
playerPassive = 'save/savePassive.txt'

def search():
    common.clear()
    repeat = random.randrange(9, 12)
    for x in range(6, repeat):
        common.clear()
        print('\n Hunting for an enemy.')
        time.sleep((0.5))
        common.clear()
        print('\n Hunting for an enemy..')
        time.sleep((0.5))
        common.clear()
        print('\n Hunting for an enemy...')
        time.sleep((0.5))

    print('\n Enemy found! The battle begins!')
    time.sleep(3)

def enemyRarityEvent(enemy):
    enemyRoll = random.randrange(1,10001)
    print(enemyRoll, 'ln-32')
    if enemyRoll < 7501:
        return enemy
    elif enemyRoll > 7500 and enemyRoll < 8501:
        enemyName = enemy[0]
        enemy[0] = 'Uncommon ' + enemyName
        enemy[2] = int(enemy[2] * 1.2)
        enemy[3] = int(enemy[3] * 1.2)
        enemy[4] = int(enemy[4] * 1.2)
        enemy[5] = int(enemy[5] * 1.2)
        enemy[6] = int(enemy[6] * 1.2)
        enemy[7] = int(enemy[7] * 1.2)
        return enemy
    elif enemyRoll > 8500 and enemyRoll < 9001:
        enemyName = enemy[0]
        enemy[0] = 'Rare ' + enemyName
        enemy[2] = int(enemy[2] * 1.5)
        enemy[3] = int(enemy[3] * 1.5)
        enemy[4] = int(enemy[4] * 1.5)
        enemy[5] = int(enemy[5] * 1.5)
        enemy[6] = int(enemy[6] * 1.5)
        enemy[7] = int(enemy[7] * 1.5)
        return enemy
    elif enemyRoll > 9000 and enemyRoll < 9401:
        enemyName = enemy[0]
        enemy[0] = 'Exquisite ' + enemyName
        enemy[2] = int(enemy[2] * 2)
        enemy[3] = int(enemy[3] * 2)
        enemy[4] = int(enemy[4] * 2)
        enemy[5] = int(enemy[5] * 2)
        enemy[6] = int(enemy[6] * 2)
        enemy[7] = int(enemy[7] * 2)
        return enemy
    elif enemyRoll > 9400 and enemyRoll < 9701:
        enemyName = enemy[0]
        enemy[0] = 'Ungodly ' + enemyName
        enemy[2] = int(enemy[2] * 3)
        enemy[3] = int(enemy[3] * 3)
        enemy[4] = int(enemy[4] * 3)
        enemy[5] = int(enemy[5] * 3)
        enemy[6] = int(enemy[6] * 3)
        enemy[7] = int(enemy[7] * 3)
        return enemy
    elif enemyRoll > 9700 and enemyRoll < 9901:
        enemyName = enemy[0]
        enemy[0] = 'Godly ' + enemyName
        enemy[2] = int(enemy[2] * 5)
        enemy[3] = int(enemy[3] * 5)
        enemy[4] = int(enemy[4] * 5)
        enemy[5] = int(enemy[5] * 5)
        enemy[6] = int(enemy[6] * 5)
        enemy[7] = int(enemy[7] * 5)
        return enemy
    elif enemyRoll > 9900 and enemyRoll < 10001:
        enemyName = enemy[0]
        enemy[0] = 'Legendary ' + enemyName
        enemy[2] = int(enemy[2] * 8)
        enemy[3] = int(enemy[3] * 8)
        enemy[4] = int(enemy[4] * 8)
        enemy[5] = int(enemy[5] * 8)
        enemy[6] = int(enemy[6] * 8)
        enemy[7] = int(enemy[7] * 8)
        return enemy

def enemyEvenEvent(enemy, playerLevel):
    # Set enemy level to be flexable
    if enemy[1] < playerLevel:
        startRange = enemy[1]
        adjustLevel = random.randrange(enemy[1], playerLevel + 1)
        adjustActual = adjustLevel - enemy[1]

        # Set enemy's new level
        enemy[1] = adjustLevel

        # Adjust stats per level up
        for levelUp in range(startRange, enemy[1] + 1):
            enemy[2] = int(enemy[2] * 1.2)
            enemy[3] = int(enemy[3] * 1.2)
            enemy[4] = int(enemy[4] * 1.2)
            enemy[5] = int(enemy[5] * 1.2)
            enemy[6] = int(enemy[6] * 1.2)
            enemy[7] = int(enemy[7] * 1.2)

        levelVar = '[Level ' + str(enemy[1]) + ']'
        enemy[0] = enemy[0].replace('[Level]', levelVar)
        return enemy

    else:
        levelVar = '[Level ' + str(enemy[1]) + ']'
        enemy[0] = enemy[0].replace('[Level]', levelVar)
        return enemy

def battleProcess(playerStats, playerSkills):

    # Initialize Variables
    enemyInfo = {
        "enemyName": '',
        "enemyLevel": 0,
        "enemyHP": 0,
        "enemyAtk": 0,
        "enemyDef": 0,
        "enemyMAtk": 0,
        "enemyMDef": 0,
        "enemySpe": 0,
        "enemySkills": [0]
    }

    playerInfo = {
        "playerLevel": playerStats[0],
        "playerExp": playerStats[1],
        "playerMoney": playerStats[2],
        "playerHP": playerStats[3],
        "playerSP": playerStats[4],
        "playerAtk": playerStats[5],
        "playerDef": playerStats[6],
        "playerMAtk": playerStats[7],
        "playerMDef": playerStats[8],
        "playerSpe": playerStats[9],
        "playerRBP": playerStats[10]
    }

    playerRebirthReward = False

    loadPassive = saveload.loadPassive(playerPassive)

    # Rebuilds dictionary to player's selection
    playerMaxHP = playerInfo['playerHP']
    playerMaxSP = playerInfo['playerSP']

    # Player's Skill Build
    playerActions = []
    with open(playerSkills, 'r') as skills:
        for line in skills:
            line = line.replace('\n', '')
            line = line.split(',')
            playerActions.append(line)

    fleeaction = ['Run', 'E', 0, 0, 'none', -1]
    playerActions.append(fleeaction)

    # Builds enemy stats
    enemyEncounterListAll = []
    enemyEncounter = []
    for name, stats in enemyInfoDict.items():
        enemyEncounterSetup = []
        for items in stats.values():
            enemyEncounterSetup.append(items)

        enemyEncounterListAll.append(enemyEncounterSetup)

    fightList = []
    for enemyList in enemyEncounterListAll:
        if enemyList[1] <= playerInfo['playerLevel']:
            fightList.append(enemyList)

    selectEnemyRandom = random.randrange(0, len(fightList))
    selectEnemy = fightList[selectEnemyRandom]

    # Adjusts enemy information
    selectEnemy = enemyRarityEvent(selectEnemy)
    selectEnemy = enemyEvenEvent(selectEnemy, playerInfo['playerLevel'])

    # Set enemy pulled to dictionary
    enemyInfo["enemyName"] = selectEnemy[0]
    enemyInfo["enemyLevel"] = selectEnemy[1]
    enemyInfo["enemyHP"] = selectEnemy[2]
    enemyInfo["enemyAtk"] = selectEnemy[3]
    enemyInfo["enemyDef"] = selectEnemy[4]
    enemyInfo["enemyMAtk"] = selectEnemy[5]
    enemyInfo["enemyMDef"] = selectEnemy[6]
    enemyInfo["enemySpe"] = selectEnemy[7]
    enemyInfo["enemySkills"] = selectEnemy[8]
    enemyMaxHP = enemyInfo['enemyHP']

    # Set up enemy actions
    enemyActionList = []
    for name, skill in enemySkillsDict.items():
        enemyActionListSetup = []
        for enemySkills in enemyInfo['enemySkills']:
            if enemySkills == name:
                for values in skill.values():
                    enemyActionListSetup.append(values)

                enemyActionList.append(enemyActionListSetup)

        else:
            pass

    # Begin battle loop
    while playerInfo['playerHP'] > 0 and enemyInfo['enemyHP'] > 0:

        '''# Player SP passive recovery
        if playerInfo['playerSP'] < playerMaxSP:
            playerInfo['playerSP'] += int(playerMaxSP * 0.1)

            # If SP recovery goes over max SP
            if playerInfo['playerSP'] > playerMaxSP:
                playerInfo['playerSP'] = playerMaxSP

        # Pass if SP at max
        else:
            pass'''

        passIntoBars = [playerInfo['playerHP'], playerMaxHP, playerInfo['playerSP'], playerMaxSP,
                        enemyInfo['enemyHP'], enemyMaxHP]

        drawBars(passIntoBars, enemyInfo['enemyName'])

        print(' Choose your battle action! \n')

        # Print battle options for player
        # Need to format skills in skills file
        actionNum = 1
        actionLineFormat = ' {}  |  {:<15} | SP Cost: {:<3} '
        for actionLine in playerActions:
            print(actionLineFormat.format(str(actionNum), actionLine[0], actionLine[2]))
            actionNum += 1

        actionInput = input('\n Select action: ')

        try:
            actionInput = int(actionInput)

            # Check player input against skill option
            if actionInput in range(1, len(playerActions) + 1):
                actionInput -= 1

                # Set action to player choice
                loadedAction = playerActions[actionInput]

                # Check if physical or special
                if loadedAction[1] == 'p':
                    pullStatPlayer = playerInfo['playerAtk']
                    pullStatEnemy = enemyInfo['enemyDef']
                elif loadedAction[1] == 'm':
                    pullStatPlayer = playerInfo['playerMAtk']
                    pullStatEnemy = enemyInfo['enemyMDef']
                else:
                    # This is for specials that boost stats, lower stats, or inflict ailments
                    pass

                damage = int((int(pullStatPlayer) * float(loadedAction[3])) - int(pullStatEnemy))
                damageVariantLow = int(damage * (-0.20))
                damageVariantHigh = int(damage * 0.21)
                if damageVariantLow > -1:
                    damageVariantLow = -1
                if damageVariantHigh < 1:
                    damageVariantHigh = 1
                damageVariant = random.randrange(damageVariantLow, damageVariantHigh)
                finalDamage = damage + damageVariant

                # Check if damage is below minimum
                if finalDamage < 1:
                    finalDamage = 1

                playerDamageLine = ' You hit the ' + enemyInfo['enemyName'] + ' for ' + str(finalDamage) + ' damage.'
                enemyInfo['enemyHP'] -= finalDamage
                playerInfo['playerSP'] -= int(loadedAction[2])
                print(playerDamageLine)
                time.sleep(1)

                # Check if enemy still has HP
                if enemyInfo['enemyHP'] > 0:

                    # Move on to enemy action
                    loadedEnemyAction = []

                    enemyAction = random.randrange(0, len(enemyActionList))
                    loadedEnemyAction = enemyActionList[enemyAction]

                    # Check if physical or special
                    if loadedEnemyAction[1] == 'p':
                        pullStatEnemy = enemyInfo['enemyAtk']
                        pullStatPlayer = playerInfo['playerAtk']
                    else:
                        pullStatEnemy = enemyInfo['enemyMAtk']
                        pullStatPlayer = playerInfo['playerMDef']

                    damage = int((int(pullStatEnemy) * loadedEnemyAction[2]) - int(pullStatPlayer))
                    damageVariantLow = int(damage * (-0.20))
                    damageVariantHigh =int(damage * 0.21)
                    if damageVariantLow > -1:
                        damageVariantLow = -1
                    if damageVariantHigh < 1:
                        damageVariantHigh = 1
                    damageVariant = random.randrange(damageVariantLow, damageVariantHigh)
                    finalDamage = damage + damageVariant

                    # Check if damage is below minimum
                    if finalDamage < 1:
                        finalDamage = 1

                    enemyDamageLine = ' You were hit by ' + enemyInfo['enemyName'] + "'s " + loadedEnemyAction[0] +\
                                      ' for ' + str(finalDamage) + ' damage.'
                    print(enemyDamageLine)
                    time.sleep(1)

                    playerInfo['playerHP'] -= finalDamage

                else:
                    pass

            else:
                print(' Invalid choice. IF LINE')
                time.sleep(2)


        except:
            print(' Invalid input. EXCEPT LINE')
            time.sleep(1)

    # Give rewards
    if playerInfo['playerHP'] > 0:

        # After battle recovery
        playerInfo['playerHP'] = playerMaxHP
        playerInfo['playerSP'] = playerMaxSP

        # Calculate experience gained
        if playerInfo['playerLevel'] < loadPassive[0]:
            expMultiplier = enemyInfo['enemyLevel'] - (playerInfo['playerLevel'] * 0.33)
            experienceReward = int(5 + (3 * expMultiplier))
            moneyMultiplier = ((enemyInfo['enemyLevel'] * 2) - playerInfo['playerLevel']) * 1.3
            moneyReward = int(3 * moneyMultiplier)

            # Prevents negative experience and guarantees reward if player isn't max level
            if experienceReward < 1:
                experienceReward = 1

            if enemyInfo['enemyLevel'] == loadPassive[0]:
                playerRebirthReward = True

        else:
            experienceReward = 0
            moneyMultiplier = ((enemyInfo['enemyLevel'] * 2) - playerInfo['playerLevel']) * 1.3
            moneyReward = int(3 * moneyMultiplier)

        # Prevents negative money and guarantees reward
        if moneyReward < 1:
            moneyReward = 1
        playerInfo['playerExp'] += experienceReward
        playerInfo['playerMoney'] += moneyReward

        print(' You gained ' + str(experienceReward) + ' exp!')
        print(' You gained ' + str(moneyReward) + ' muns!')
        if playerRebirthReward:
            playerInfo['playerRBP'] += 10
            print(' You beat a max level monster! You earned 10 rebirth!')
        if 'Godly' in enemyInfo['enemyName']:
            playerInfo['playerRBP'] += 50
            print(' You beat a Godly enemy! You earned 50 rebirth!')
        if 'Legendary' in enemyInfo['enemyName']:
            playerInfo['playerRBP'] += 250
            print(' You defeated a legendary enemy! You earned 250 rebirth!')
        time.sleep(1)

        # Player levels up
        if playerInfo['playerExp'] >= 100:
            if playerInfo['playerLevel'] < loadPassive[0]:
                print('\n You have leveled up!')
                levelup.levelUp(playerInfo)
                playerInfo['playerExp'] -= 100
            else:
                print(' You have reached max level for this life.')
                time.sleep(2)

        if playerInfo['playerLevel'] == loadPassive[0]:
            playerInfo['playerExp'] = 0

        # Save after fight
        playerNumbers = []
        for value in playerInfo.values():
            value = int(value)
            playerNumbers.append(value)

        saveload.save(playerFile, playerNumbers)
        return playerNumbers

    # If defeated
    else:
        print(' You were defeated. Returning to main menu.')
        time.sleep(2)

        playerNumbers = []
        playerInfo['playerHP'] = playerMaxHP
        playerInfo['playerSP'] = playerMaxSP

    for value in playerInfo.values():
        value = int(value)
        playerNumbers.append(value)

    return playerNumbers

def drawBars(collect, enemyName):
    common.clear()
    playerHP = collect[0]
    playerMaxHP = collect[1]
    playerSP = collect[2]
    playerMaxSP = collect[3]
    enemyHP = collect[4]
    enemyMaxHP = collect[5]

    # Use percent to generate number of blocks for bars
    playerHPPercent = int((playerHP / playerMaxHP) * 15)
    playerSPPercent = int((playerSP / playerMaxSP) * 15)
    enemyHPPercent = int((enemyHP / enemyMaxHP) * 20)

    # Check is player and enemy have more than 1 HP but percent calculation gives 0
    if playerHPPercent == 0 or playerSPPercent == 0 or enemyHPPercent == 0:
        if playerHP > 0 and playerHPPercent == 0:
            playerHPPercent = 1
        if playerSP > 0 and playerSPPercent == 0:
            playerSPPercent = 1
        if enemyHP > 0 and enemyHPPercent == 0:
            enemyHPPercent = 1

    # Set up template for bar printing

    playerHPDisplay = str(playerHP) + ' / ' + str(playerMaxHP)
    playerSPDisplay = str(playerSP) + ' / ' + str(playerMaxSP)

    if len(playerHPDisplay) > len(playerSPDisplay):
        lengthInsert = 16 + len(playerHPDisplay)
    else:
        lengthInsert = 16 + len(playerSPDisplay)

    # Moves enemy bar to better align with growing player info
    enemyLineZero = ' ' * lengthInsert + '{:>23}'
    enemyLineOne = ' ' * lengthInsert + '║ [{:>20}] ║'
    enemyLineTwo = ' ' * lengthInsert + '╚' + '═' * 24 + '╝'

    # Set lengths of player display to match when larger numbers are inserted
    length = '{:>' + str(lengthInsert - 16) + '}'
    playerLineData = ' ║ [{:<15}] ' + '{}' + length + ' ║'
    playerLineBottom = ' ╚' + '═' * (lengthInsert + 6) + '═╝'

    # Print bars for display
    print(enemyLineZero.format(enemyName))
    print(enemyLineOne.format('▓' * enemyHPPercent))
    print(enemyLineTwo, '\n')
    print(playerLineData.format('▓' * playerHPPercent, 'HP ', playerHPDisplay))
    print(playerLineData.format('▓' * playerSPPercent, 'SP ', playerSPDisplay))
    print(playerLineBottom)
