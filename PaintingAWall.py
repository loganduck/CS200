import math

"""
Programming in Python 3 with zyLabs
3.11 Program: Painting a wall (Python 3)
Southern New Hampshire University

logan.duck@snhu.edu
"""
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))

wallArea = wallHeight * wallWidth
print('Wall area:', wallArea, 'square feet')

paintNeeded = wallArea / 350
print('Paint needed:', paintNeeded, 'gallons')

cansNeeded = math.ceil(paintNeeded)
print('Cans needed:', cansNeeded, 'can(s)', '\n')

color = input('Choose a color to paint the wall: \n')

totalPrice = '$' + str(cansNeeded * paintColors.get(color))
print('Cost of purchasing', color, 'paint:', totalPrice)