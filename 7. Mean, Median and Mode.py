# This script will calcualte and print the mean, median and mode of a given set_of_numbers

set_of_numbers = [-105,-105, -105, -105, -105, -103,-103,-103,-103, -103, -5, 123 ,1,1,1,1,1,1,1,1,1,1, 2, 3, 4, 100, 2000, 3000]

def mean(a):
    return sum(a)/len(a)


def median(b):
    b = sorted(b)
    medianVal = []
    medianVal2 = 0
    if len(b)%2 == 0:
        medianVal.append(round(len(b)/2))
        medianVal.append(medianVal[0]-1)
        medianVal2 = (b[medianVal[0]]+b[medianVal[1]])/2
    else:
        medianVal2 = len(b)/2
        medianVal2 = b[int(medianVal2)]
    return medianVal2


def mode(c):
    mode_numbers = sorted([[c.count(x), x] for x in set(c)])
    mode_numbers_two = []
    highest_count = mode_numbers[-1][0]
    for i in range(len(mode_numbers)-1,0,-1):
        if highest_count == mode_numbers[i][0]:
            mode_numbers_two.append(mode_numbers[i][1])
        else:
            break
    return mode_numbers_two

print(mean(set_of_numbers))
print(median(set_of_numbers))
print(mode(set_of_numbers))
