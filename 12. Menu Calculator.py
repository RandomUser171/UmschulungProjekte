# This script calculates the total value order according the the user's input



# Menu list
menu_items = [
    ('Chicken Strips' , 3.50),
    ('French Fries' , 2.50),
    ('Hamburger' , 4.00),
    ('Hotdog' , 3.50),
    ('Large Drink' , 1.75),
    ('Medium Drink' , 1.50),
    ('Milk Shake' , 2.25),
    ('Salad' , 3.75),
    ('Small Drink' , 1.25)]

# Valid input
numbers = '123456789'



def menu_calculator():
    
    # Prints the Menu
    for i in range(len(menu_items)):
        print(str(i+1)+'.', menu_items[i][0],' '*2,'-',' '*2, menu_items[i][1])
        
    
    print('Please enter the order.')
    

    is_it_ok = False
    quantity_of_items = {}
    
    # Loop to check if input is valid
    while is_it_ok == False:
        order = input()
        is_it_ok = True
        
        
       # Checks if the input is valid
        for i in order:
            if i not in numbers:
                print('Please enter positive integers only.')
                is_it_ok = False
                break
                
                
    order_value = 0
    
    # Calculates and prints the total value of the order
    for i in set(order):
        quantity_of_items[menu_items[int(i)-1][0]] = 0
    for i in order:
        quantity_of_items[menu_items[int(i)-1][0]] += 1
        order_value += menu_items[int(i)-1][1]
    for i in quantity_of_items:
        print(i)
        print(quantity_of_items[i],'  :  ',quantity_of_items[i])
    print('$%.2f'%(order_value))
    
    # Asks the user if they want to repeat the program
    print('Would you like to enter another order? Type "y" to repeat.')
    repeat = input()
    if repeat.lower() == 'y':
        menu_calculator()



menu_calculator()
