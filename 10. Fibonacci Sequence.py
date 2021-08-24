def fibonacci_sequence(n):
    list = [0,1]
    if n >2:
        for i in range(1,n):
            list.append(list[i]+list[i-1])
    print(list)
    print(list[n])





fibonacci_sequence(15)