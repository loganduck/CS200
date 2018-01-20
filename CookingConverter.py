"""
Programming in Python 3 with zyLabs
2.12 Program: Cooking measurement converter (Python 3)
Southern New Hampshire University

logan.duck@snhu.edu
"""

lemonJuiceCups = float(input('Enter amount of lemon juice (in cups): \n'))
water = float(input('Enter amount of water (in cups): \n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups): \n'))
servings = float(input('How many servings does this make? \n'))

print('\nLemonade ingredients - yields', servings, 'servings')
print(lemonJuiceCups, 'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agave_nectar, 'cup(s) agave nectar\n')

desired_servings = float(input('How many servings would you like to make? \n'))

print('\nLemonade ingredients - yields', desired_servings, 'servings')
serving_adjustment = desired_servings / servings

lemonJuiceCups = lemonJuiceCups * serving_adjustment
water = water * serving_adjustment
agave_nectar = agave_nectar * serving_adjustment

print(lemonJuiceCups, 'cup(s) lemon juice')
print(water, 'cup(s) water')
print(agave_nectar, 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', desired_servings, 'servings')
lemon_gal = lemonJuiceCups / 16
water_gal = water / 16
agave_gal = agave_nectar / 16

print(lemon_gal, 'gallon(s) lemon juice')
print(water_gal, 'gallon(s) water')
print(agave_gal, 'gallon(s) agave nectar')