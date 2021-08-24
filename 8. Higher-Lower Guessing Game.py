import random

number = 0
max_number = 100

def game():
    number = random.randint(1,max_number)
    print('Be a psychic and guess what number the computer is thinking!\n Enter an integer between 1 and %d'%(max_number))
    number_guessed = inputValue(max_number)
    tries = 1
    while number != number_guessed:
        if number<number_guessed:
            print('Try a lower number')
        else:
            print('Try a bigger number')
        number_guessed = int(input())
        tries +=1
    print('You found the number!\n The number was %d and it took you %d tries'%(number, tries))
    play_again = input('Would you like to play again? Type "y" to repeat the game: ')
    if play_again.lower() == 'y':
        game()

def inputValue(numberVal):
    try:
        guessedValue = int(input())
    except ValueError:
        print('Please enter an INTEGER between 1 and %d'%(numberVal))
        guessedValue = inputValue(numberVal)
    if guessedValue > 0 and guessedValue <=numberVal:
        return guessedValue
    else:
        print('Please enter an integer BETWEEN 1 and %d (inclusive)'%(numberVal))
        return inputValue(numberVal)

game()