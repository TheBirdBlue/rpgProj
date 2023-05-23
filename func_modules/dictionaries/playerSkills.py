"""
Default Template

    'Name': {
        'displayName': '',
        'type': 'p/m/e',
        'spCost': int,
        'power': int,
        'element': 'fire/water/earth/air/dark/light/none'
        'special': int,
        'rbCost': int
    },


"""

playerSkillsDict = {
    'Attack': {
        'displayName': 'Attack',
        'type': 'p',
        'spCost': 0,
        'power': 1.5,
        'element': 'none',
        'special': 0,
        'rbCost': 0
    },
    'Slash': {
        'displayName': 'Slash',
        'type': 'p',
        'spCost': 2,
        'power': 2,
        'element': 'none',
        'special': 0,
        'rbCost': 50
    },
    'Flare': {
        'displayName': 'Flare',
        'type': 'm',
        'spCost': 3,
        'power': 2,
        'element': 'fire',
        'special': 0,
        'rbCost': 75
    },
    'Spark': {
        'displayName': 'Spark',
        'type': 'm',
        'spCost': 3,
        'power': 2,
        'element': 'electric',
        'special': 0,
        'rbCost': 75
        },
    'Drip': {
        'displayName': 'Drip',
        'type': 'm',
        'spCost': 3,
        'power': 2,
        'element': 'water',
        'special': 0,
        'rbCost': 75
    },
    'Dust': {
        'displayName': 'Dust',
        'type': 'm',
        'spCost': 3,
        'power': 2,
        'element': 'earth',
        'special': 0,
        'rbCost': 75
    },
    'Gust': {
        'displayName': 'Gust',
        'type': 'm',
        'spCost': 3,
        'power': 2,
        'element': 'air',
        'special': 0,
        'rbCost': 75
    }
}
