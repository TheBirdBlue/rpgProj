import time
import saveload
import common


def rebirthFunc(playerStats, playerFile, playerPassive):
    rebirth = True

    # Check if player can rebirth
    with open(playerPassive) as passive:
        passiveCheck = []
        for line in passive:
            line = int(line)
            passiveCheck.append(line)

    if playerStats[0] == passiveCheck[0]:

        # Set names
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

        # Begin the rebirth!
        while rebirth:
            print(" Rebirth will reset your charcter to level 1 but award you with one rebirth point that can be\n"
                  " spent on skills, permanant buffs, and increase your level cap. This action is permanant and\n"
                  " cannot be reversed.\n"
                  "\n")
            confirm = input(' Do you want continue? (Y or N): ')

            confirm = confirm.upper()
            if confirm == 'Y':

                # Open player's file and write to list
                with open(playerFile, 'r') as playerFile:
                    fileSetup = []
                    for line in playerFile:
                        fileSetup.append(line)

                    carryover = int(fileSetup[-1])

                # Open player's passive bonuses and write to list
                with open(playerPassive, 'r') as playerPassive:
                    passiveSetup = []
                    for line in playerPassive:
                        line = int(line)
                        passiveSetup.append(line)

                # Calculate ReBirth Bonus
                bonusLevel = int(charLvl / 20)
                bonusHP = int((charHP - 10) / 10)
                bonusSP = int((charSP - 10) / 10)
                bonusAtk = int((charAtk - 5) / 3)
                bonusDef = int((charDef - 5) / 3)
                bonusMAtk = int((charMAtk - 5) / 3)
                bonusMDef = int((charMDef - 5) / 3)
                bonusSpe = int((charSpe - 5) / 3)
                rbbonus = bonusLevel + bonusHP + bonusSP + bonusAtk + bonusDef + bonusMAtk + bonusMDef + bonusSpe

                # Recall default start values
                defaultOrder = [1, 0, 0, 10, 10, 5, 3, 5, 3, 3, 0]
                with open('save/saveOverview.txt', "w") as playerFile:
                    # Overworld Info
                    playerFile.write(str(defaultOrder[0]) + '\n')
                    playerFile.write(str(defaultOrder[1]) + '\n')
                    playerFile.write(str(defaultOrder[2]) + '\n')

                    # Stat Info
                    playerFile.write(str(defaultOrder[3] + passiveSetup[1]) + '\n')
                    playerFile.write(str(defaultOrder[4] + passiveSetup[2]) + '\n')
                    playerFile.write(str(defaultOrder[5] + passiveSetup[3]) + '\n')
                    playerFile.write(str(defaultOrder[6] + passiveSetup[4]) + '\n')
                    playerFile.write(str(defaultOrder[7] + passiveSetup[5]) + '\n')
                    playerFile.write(str(defaultOrder[8] + passiveSetup[6]) + '\n')
                    playerFile.write(str(defaultOrder[9] + passiveSetup[7]) + '\n')
                    playerFile.write(str(defaultOrder[10] + carryover + rbbonus) + '\n')

                # Grab new stats to return to main game
                returnList = []
                returnList = saveload.loadOver('save/saveOverview.txt', returnList)

                rebirth = False
                print(' Welcome to your new life...')
                time.sleep(3)

                return returnList

    else:
        expNeeded = (passiveCheck[0] - playerStats[0]) * 100 + (100 - playerStats[1])
        expNeededFormat = common.numConversion(expNeeded)
        print(' ' + expNeededFormat + ' exp until next rebirth.')
        time.sleep(2)
        return playerStats