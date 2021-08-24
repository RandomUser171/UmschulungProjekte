# Change finder
quarters = 0
dimes = 0
nickels = 0
pennies = 0


# Calculates the coins needed
def change_finder(total_coins):
    coinsNeeded = []
    for i in [25, 10, 5, 1]:  # Coins are manually here within the loop intergrated
        coinsNeeded.append(total_coins // i)
        total_coins -= (total_coins // i) * i
    return coinsNeeded


# Main program
# Has 3 main tasks
# 1. The price of the items
# 2. The continuation/termination of the program
# 3. Controls wether the correct input is given
def coin_input():
    print('Please enter the price of the item:')
    coinValueCorrect = False
    while coinValueCorrect == False:  # checks if the value is correct
        try:
            coins = float(input())
            break
        except:
            print('Please enter a number.')
    coins = int(coins * 100)
    quarters, dimes, nickels, pennies = change_finder(coins)

    print('You need %d quarters, %d dimes, %d, nickels, %d pennies!' % (quarters, dimes, nickels, pennies))
    print('Would you like to repeat? (y/n)')
    repeat_input = input()
    while repeat_input.lower() != 'y' and repeat_input.lower() != 'n':  # checks if the value is correct
        print('Please enter "y" or "n" ')
        repeat_input = input()
    if repeat_input.lower() == 'y':
        coin_input()
    else:
        print('Program terminated')


coin_input()