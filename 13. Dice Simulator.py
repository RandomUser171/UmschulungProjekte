import random

def input_def(min,max,print_string):
    '''
    This function makes sure the value of the input is within the limits specified and then returns it
    '''
    while True:
        input_value = input('Please enter the %s. :'%(print_string))
        try:
            if int(input_value) >=min and int(input_value) <max+1:
                return int(input_value)
            else:
                print('Please enter an integer between %d and %d (inclusive).' % (min, max))
        except:
            print('Please enter an integer between %d and %d (inclusive).'%(min,max))

def simulate_rolls(sides,rolls):
    '''
    This function simulates the rolls of the dice and then returns the outcomes as well as tracks and returns how many times an outcome was seen
    '''
    list_of_outcomes = []
    for i in range(rolls):
        list_of_outcomes.append(random.randint(1,sides))
    return list_of_outcomes



def main():
    while True:
        print('Welcome to this dice simulator.\n Please enter how many sides the dice has (3-20) and how many times you want it to be rolled (1-1,000,000)')
        number_of_sides = input_def(3,20,'number of dice\'s sides')
        number_of_rolls = input_def(1,1000000,'number of rolls')
        simulated_rolls = simulate_rolls(number_of_sides,number_of_rolls)
        groupped_simulated_rolls = []
        percentages_of_simulated_rolls = []
        print(simulated_rolls)
        for i in range(1,number_of_sides+1):
            groupped_simulated_rolls.append(simulated_rolls.count(i))
        print(groupped_simulated_rolls)
        for i in range(len(groupped_simulated_rolls)):
            percentages_of_simulated_rolls.append(groupped_simulated_rolls[i]/number_of_rolls)
        for i in range(number_of_sides):
            print('The percentage of the number %d was %%%.2f.'%(i+1,percentages_of_simulated_rolls[i]))
        print('Would you like to play repeat the program? Type "y" to repeat.')
        repeat_program = input()
        if repeat_program.lower() != 'y':
            break


if __name__ == '__main__':main()

