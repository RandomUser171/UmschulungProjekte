"""
@author: Thanasis
"""


# Receives the user's input, converts it to integer (c)
def user_input():
    xAsInteger = None
    while isinstance(xAsInteger, int) == False:
        x = input()
        try:
            xAsInteger = int(x)
        except:
            print('Please enter an integer.\n')
    return xAsInteger


# Asks the user for the 3 sides of the triangle
# and sorts the hypotenuse (c)
def questionPrompter():
    
    print('Please enter the first side of the triangle:')
    a = abs(user_input())
    print('Please enter the second side of the triangle:')
    b = abs(user_input())
    print('Please enter the third side of the triangle:')
    c = abs(user_input())
    
    
    triangleSides = [a, b, c]
    triangleSides.sort()
    
    
    if (triangleSides[2] ** 2) == (triangleSides[1] ** 2) + (triangleSides[0] ** 2): 
        print('Ya did it')
    else:
        print("ya didn't do it")
        
        
    print('Would you like to try again? (y/n)')
    
    x = input()
    while x != 'y' and x != "n":
        print('Would you like to try again? (y/n)')
        x = input()
    if x == 'y':
        questionPrompter()
    else:
        return


questionPrompter()
