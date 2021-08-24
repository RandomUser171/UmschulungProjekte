bottles = 'bottles'
bottles2 = 'bottles'
n = 100
for i in range(n, 0, -1):
    if i == 1:
        bottles = 'bottle'
    else:
        bottles = 'bottles'
    if i - 1 == 1:
        bottles2 = 'bottle'
    else:
        bottles2 = 'bottles'

    print(
        '%d %s of beer on the wall, %d %s of beer. \nTake one down and pass it around, %d %s of beer on the wall.\n' % (
        i, bottles, i, bottles, i - 1, bottles2))