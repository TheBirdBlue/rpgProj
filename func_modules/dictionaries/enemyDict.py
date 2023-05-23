'''

    ID: {
        "enemyName": '[Level] ',
        "enemyLevel": int,
        "enemyHP": int,
        "enemyAtk": int,
        "enemyDef": int,
        "enemyMAtk": int,
        "enemyMDef": int,
        "enemySpe": int,
        "enemySkills": [0]
    },

'''

enemyInfoDict = {
    1: {
        "enemyName": '[Level] Rat',
        "enemyLevel": 1,
        "enemyHP": 5,
        "enemyAtk": 7,
        "enemyDef": 2,
        "enemyMAtk": 3,
        "enemyMDef": 2,
        "enemySpe": 3,
        "enemySkills": [0]
    },
    2: {
        "enemyName": '[Level] Slime',
        "enemyLevel": 1,
        "enemyHP": 6,
        "enemyAtk": 5,
        "enemyDef": 3,
        "enemyMAtk": 3,
        "enemyMDef": 1,
        "enemySpe": 3,
        "enemySkills": [0, 12]
    },
    3: {
        "enemyName": '[Level] Goblin',
        "enemyLevel": 1,
        "enemyHP": 10,
        "enemyAtk": 7,
        "enemyDef": 1,
        "enemyMAtk": 1,
        "enemyMDef": 1,
        "enemySpe": 3,
        "enemySkills": [0, 1]
    },
    4: {
        "enemyName": '[Level] Novice Mage',
        "enemyLevel": 1,
        "enemyHP": 10,
        "enemyAtk": 2,
        "enemyDef": 3,
        "enemyMAtk": 5,
        "enemyMDef": 3,
        "enemySpe": 5,
        "enemySkills": [0, 10, 11, 12, 13, 14]
    },
    5: {
        "enemyName": '[Level] Mini Golem',
        "enemyLevel": 1,
        "enemyHP": 16,
        "enemyAtk": 2,
        "enemyDef": 5,
        "enemyMAtk": 1,
        "enemyMDef": 2,
        "enemySpe": 1,
        "enemySkills": [0, 1]
        },
    6: {
        "enemyName": '[Level] Salamander',
        "enemyLevel": 1,
        "enemyHP": 11,
        "enemyAtk": 6,
        "enemyDef": 3,
        "enemyMAtk": 5,
        "enemyMDef": 2,
        "enemySpe": 5,
        "enemySkills": [0, 1, 10]
    },
    7: {
        "enemyName": '[Level] Nymph',
        "enemyLevel": 1,
        "enemyHP": 12,
        "enemyAtk": 4,
        "enemyDef": 4,
        "enemyMAtk": 3,
        "enemyMDef": 4,
        "enemySpe": 5,
        "enemySkills": [0, 12]
    },
    8: {
        "enemyName": '[Level] Boar',
        "enemyLevel": 1,
        "enemyHP": 20,
        "enemyAtk": 8,
        "enemyDef": 2,
        "enemyMAtk": 1,
        "enemyMDef": 1,
        "enemySpe": 4,
        "enemySkills": [0, 9]
    },
    9: {
        "enemyName": '[Level] Fighter',
        "enemyLevel": 1,
        "enemyHP": 10,
        "enemyAtk": 8,
        "enemyDef": 3,
        "enemyMAtk": 2,
        "enemyMDef": 2,
        "enemySpe": 5,
        "enemySkills": [0, 4, 5]
    },
    10: {
        "enemyName": '[Level] Goblin',
        "enemyLevel": 2,
        "enemyHP": 14,
        "enemyAtk": 11,
        "enemyDef": 4,
        "enemyMAtk": 7,
        "enemyMDef": 4,
        "enemySpe": 6,
        "enemySkills": [0]
        },
    11: {
        "enemyName": '[Level] Bandit',
        "enemyLevel": 2,
        "enemyHP": 15,
        "enemyAtk": 7,
        "enemyDef": 4,
        "enemyMAtk": 7,
        "enemyMDef": 4,
        "enemySpe": 6,
        "enemySkills": [0, 1]
    },
    12: {
        "enemyName": '[Level] Undead',
        "enemyLevel": 2,
        "enemyHP": 16,
        "enemyAtk": 8,
        "enemyDef": 1,
        "enemyMAtk": 1,
        "enemyMDef": 1,
        "enemySpe": 1,
        "enemySkills": [0]
        },
    13: {
        "enemyName": '[Level] Spider',
        "enemyLevel": 2,
        "enemyHP": 15,
        "enemyAtk": 7,
        "enemyDef": 4,
        "enemyMAtk": 4,
        "enemyMDef": 3,
        "enemySpe": 4,
        "enemySkills": [0]
    },
    14: {
        "enemyName": '[Level] Froggert',
        "enemyLevel": 2,
        "enemyHP": 18,
        "enemyAtk": 8,
        "enemyDef": 3,
        "enemyMAtk": 5,
        "enemyMDef": 3,
        "enemySpe": 4,
        "enemySkills": [0, 4]
    },
    15: {
        "enemyName": '[Level] Wolf',
        "enemyLevel": 1,
        "enemyHP": 11,
        "enemyAtk": 5,
        "enemyDef": 4,
        "enemyMAtk": 2,
        "enemyMDef": 2,
        "enemySpe": 3,
        "enemySkills": [0]
    },
    16: {
        "enemyName": '[Level] Coyote',
        "enemyLevel": 2,
        "enemyHP": 17,
        "enemyAtk": 7,
        "enemyDef": 4,
        "enemyMAtk": 3,
        "enemyMDef": 3,
        "enemySpe": 3,
        "enemySkills": [0]
    },
    17: {
        "enemyName": '[Level] Harpy',
        "enemyLevel": 2,
        "enemyHP": 24,
        "enemyAtk": 6,
        "enemyDef": 4,
        "enemyMAtk": 4,
        "enemyMDef": 3,
        "enemySpe": 3,
        "enemySkills": [0, 2, 3, 14]
    },
    18: {
        "enemyName": '[Level] Wasp',
        "enemyLevel": 2,
        "enemyHP": 20,
        "enemyAtk": 8,
        "enemyDef": 2,
        "enemyMAtk": 4,
        "enemyMDef": 2,
        "enemySpe": 4,
        "enemySkills": [0, 3]
    },
    19: {
        "enemyName": '[Level] Finder',
        "enemyLevel": 2,
        "enemyHP": 18,
        "enemyAtk": 7,
        "enemyDef": 5,
        "enemyMAtk": 4,
        "enemyMDef": 4,
        "enemySpe": 5,
        "enemySkills": [0, 6]
    },
    20: {
        "enemyName": '[Level] Wild Boar',
        "enemyLevel": 3,
        "enemyHP": 29,
        "enemyAtk": 14,
        "enemyDef": 5,
        "enemyMAtk": 1,
        "enemyMDef": 1,
        "enemySpe": 8,
        "enemySkills": [0, 3]
    },
    21: {
        "enemyName": '[Level] Mush Cap',
        "enemyLevel": 3,
        "enemyHP": 26,
        "enemyAtk": 9,
        "enemyDef": 5,
        "enemyMAtk": 6,
        "enemyMDef": 5,
        "enemySpe": 5,
        "enemySkills": [0, 6, 13]
    },
    22: {
        "enemyName": '[Level] Living Sword',
        "enemyLevel": 3,
        "enemyHP": 10,
        "enemyAtk": 11,
        "enemyDef": 9,
        "enemyMAtk": 1,
        "enemyMDef": 1,
        "enemySpe": 1,
        "enemySkills": [0, 1]
    },
    23: {
            "enemyName": '[Level] Living Armor',
            "enemyLevel": 4,
            "enemyHP": 30,
            "enemyAtk": 6,
            "enemyDef": 12,
            "enemyMAtk": 4,
            "enemyMDef": 8,
            "enemySpe": 2,
            "enemySkills": [0, 9]
        },
    24: {
        "enemyName": '[Level] Mimic',
        "enemyLevel": 4,
        "enemyHP": 48,
        "enemyAtk": 9,
        "enemyDef": 10,
        "enemyMAtk": 9,
        "enemyMDef": 10,
        "enemySpe": 5,
        "enemySkills": [0, 13]
    },
}
