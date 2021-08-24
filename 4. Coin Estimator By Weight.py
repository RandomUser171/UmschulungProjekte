# -*- coding: utf-8 -*-
"""
@author: Thanasis
"""

# (W)eights in grams
penniesW = 2.5
nickelsW = 5
dimesW = 2.268
quartersW = 5.670
# Gram to Pounds conversion is 1g/453.59237

# Coin Wrappers
penny = 50
nickel = 40
dime = 50
quarter = 40


def select_coins():
    print('Please enter one of the following type of coins:')
    print('"p" for Pennies')
    print('"n" for Nickels')
    print('"d" for Dimes')
    print('"q" for Quarters')
    x = input('Enter your choice here: ')
    while x != 'p' and x != 'n' and x != 'd' and x != 'q':
        x = input('Please enter one of the values(p, n, d, q): ')
    if x == 'p':
        return penniesW, 'p'
    elif x == 'n':
        return nickelsW, 'n'
    elif x == 'd':
        return dimesW, 'd'
    else:
        return quartersW, 'q'


def select_weight_measurement():
    print('Please enter one of the following type of weight measurement:')
    print('"g" for Grams')
    print('"p" for Pounds')
    x = input('Enter your choice here: ')
    while x != 'g' and x != 'p':
        x = input('Please enter one of the values(g, p): ')
    return x


def input_weight():
    xAsInteger = None
    while isinstance(xAsInteger, int) == False:
        x = input()
        try:
            xAsInteger = int(x)
        except:
            print('Please enter an integer.\n')
    return xAsInteger


def questionPrompt():
    a, coinType = select_coins()
    b = select_weight_measurement()
    print('Please enter the weight of the coins')
    c = abs(input_weight())
    if b == 'p':
        a /= 453.59237

    totalWeight = c / a
    print(totalWeight)


questionPrompt()