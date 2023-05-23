#!/usr/bin/python

import time
import os
import sys

sys.path.insert(0, './func_modules')
sys.path.insert(1, './func_modules/dictionaries')
sys.path.insert(2, './saves')

import common
import saveload
import battleFunction
import characterShoppe
import rebirth

# File locations
fileLocationUser = 'save/saveOverview.txt'
fileLocationSkills = 'save/saveSkills.txt'
fileLocationPassive = 'save/savePassive.txt'

choiceList = ['Adventure', 'Character Shoppe', 'Rebirth', 'Options', 'Quit']

def maingame():

    run = True

    # Set Character values before loading
    charLvl = 0
    charExp = 0
    charMun = 0
    charHP = 0
    charSP = 0
    charAtk = 0
    charDef = 0
    charMAtk = 0
    charMDef = 0
    charSpe = 0
    charRebirth = 0

    loadList = []

    # Load or create save files
    if os.path.exists(fileLocationUser) == False:
        workingOverview = saveload.createOver(fileLocationUser, charLvl, charExp, charMun, charHP, charSP, charAtk,
                                              charDef, charMAtk,charMDef, charSpe, charRebirth)
        saveload.createSkill(fileLocationSkills)
        workingPassive = saveload.createPassive(fileLocationPassive)
        common.clear()
    else:
        workingOverview = saveload.loadOver(fileLocationUser, loadList)
        workingPassive = saveload.loadPassive(fileLocationPassive)
        common.clear()

    while run == True:
        # Change values to created and loaded values
        charLvl = workingOverview[0]
        charExp = workingOverview[1]
        charMun = workingOverview[2]
        charHP = workingOverview[3]
        charSP = workingOverview[4]
        charAtk = workingOverview[5]
        charDef = workingOverview[6]
        charMAtk = workingOverview[7]
        charMDef = workingOverview[8]
        charSpe = workingOverview[9]
        charMaxLevel = workingPassive[0]

        # Print general overview
        common.clear()

        # Set line formats
        infoLineChar = ' ║ Lvl:{:>3} / {:<3} ║ Mun:{:>9} ║'
        infoLineExp = ' ║ Exp:{:>25} ║'
        expAmount = int(((charExp/100)) * 21)
        expBar = ' [' + (' ' * (20 - expAmount)) + ('▓' * expAmount) + ']'
        charMunFormat = common.numConversion(charMun)
        choiceBar = ' ║ {:2} ║ {:<24} ║'

        choiceNum = 1

        # Print lines
        print(' ╔═══════════════╦═══════════════╗')
        print(infoLineChar.format(charLvl, charMaxLevel, charMunFormat))
        print(' ╠═══════════════╩═══════════════╣')
        print(infoLineExp.format(expBar))
        print(' ╠═══════════════════════════════╣')
        for options in choiceList:
            print(choiceBar.format(choiceNum, options))
            choiceNum += 1
        print(' ╚═══════════════════════════════╝')

        playerSelection = input('\n Please pick an option above: ')

        # Check player input
        #try:
        playerSelection = int(playerSelection)
        if playerSelection in range(1, len(choiceList) + 1):

            if playerSelection == 1:
                #battleFunction.search()
                workingOverview = battleFunction.battleProcess(workingOverview, fileLocationSkills)

            elif playerSelection == 2:
                workingOverview = characterShoppe.shoppeKeep(workingOverview, workingPassive)

            elif playerSelection == 3:
                workingOverview = rebirth.rebirthFunc(workingOverview, fileLocationUser, fileLocationPassive)

            elif playerSelection == 4:
                pass

            elif playerSelection == 5:
                confirm = input(' Do you want to keep playing? (Y or N): ')
                if confirm.upper() == 'N':
                    run = False
                else:
                    pass

            else:
                print(' Invalid input.')
                time.sleep(3)

        #except:
            #print(' Invalid input. Please try again.')
            #time.sleep(2)

maingame()
