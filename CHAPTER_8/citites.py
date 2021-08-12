import time
state = {
    'A1':{
        'POP':'Texas',
        'CODE':'TX',
        'FACT':'Big & hot'
    },
    'A2':{
        'POP':'Montana',
        'CODE':'MT',
        'FACT':'Mountains & blue big sky',
    },
    'A3':{
        'POP':'Washington',
        'CODE':'WS',
        'FACT':'Floooooods',
    },
        }
for key, value in state.items():
    POPULATION = value['POP']
    CC = value['CODE']
    FACT = value['FACT']
    print(f"\tState: {POPULATION.title()}")
    print(f"\tCountry Code: {CC}")
    print(f"\tFact: {FACT.upper()}\n")