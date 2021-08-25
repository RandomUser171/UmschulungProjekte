import random

file = open('11. Hangman Game words.txt','r')

words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace('\n', '')
random_word = random.randint(0,len(words)-1)
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def game(word_number):
    print('The word has been chosen and the word is %d letters long.'%(len(words[word_number])))
    word_to_be_guessed = '_'*len(words[word_number])
    already_guessed_letters = ''
    lives = 5
    while word_to_be_guessed != words[word_number]:
        letter_guess = input('Please type a letter: ')
        if letter_guess not in already_guessed_letters and len(letter_guess) ==1 and letter_guess.lower() in alphabet:
            already_guessed_letters += letter_guess
            if letter_guess in words[word_number]:
                for i in range(len(words[word_number])):
                    if words[word_number][i] == letter_guess:
                        word_to_be_guessed = word_to_be_guessed[:i]+letter_guess+word_to_be_guessed[i+1:]
                        print(word_to_be_guessed)
                        if word_to_be_guessed == words[word_number]:
                            print("You've found the word! The word was \"%s\""%(words[word_number]))
                            gameRepeat('won')
            else:
                print('Wrong letter, one life lost')
                lives -= 1
                if lives < 0:
                    print("You've lost! The word was \"%s\""%(words[word_number]))
                    gameRepeat('lost')
        else:
            print('You\'ve either guessed that letter or it\' not a single letter. Please try again')

def gameRepeat(won_or_lost):
    if won_or_lost == 'won':
        print('You\'ve won the game, would you like to play again? Type: "y" to repeat.')
    else:
        print('You\'ve lost the game, would you like to play again? Type "y" to repeat.')
    repeat_or_not = input()
    if repeat_or_not.lower() == 'y':
        game(random.randint(0,len(words)-1))



game(random_word)