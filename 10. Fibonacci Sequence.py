# This script creates an array depending on the value of the argument given and then prints it along with the last number

def fibonacci_sequence(n):
    list = [0,1]
    if n >2:
        for i in range(1,n):
            list.append(list[i]+list[i-1])
    print(list)
    print(list[n])





fibonacci_sequence(15) # 15 = size of the wished array
