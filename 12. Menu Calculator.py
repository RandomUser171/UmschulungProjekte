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
numbers = '123456789'

def menu_calculator():
    for i in range(len(menu_items)):
        print(str(i+1)+'.', menu_items[i][0],' '*2,'-',' '*2, menu_items[i][1])
    print('Please enter the order.')
    is_it_ok = False
    quantity_of_items = {}
    while is_it_ok == False:
        order = input()
        is_it_ok = True
        for i in order:
            if i not in numbers:
                print('Please enter positive integers only.')
                is_it_ok = False
                break
    order_value = 0
    for i in set(order):
        quantity_of_items[menu_items[int(i)-1][0]] = 0
    for i in order:
        quantity_of_items[menu_items[int(i)-1][0]] += 1
        order_value += menu_items[int(i)-1][1]
    for i in quantity_of_items:
        print(i)
        print(quantity_of_items[i],'  :  ',quantity_of_items[i])
    print('$%.2f'%(order_value))
    print('Would you like to enter another order? Type "y" to repeat.')
    repeat = input()
    if repeat.lower() == 'y':
        menu_calculator()



menu_calculator()