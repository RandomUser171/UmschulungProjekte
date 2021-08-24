def find_factors(n):
    factors = []
    if n > 0:
        for i in range(n):
            try:
                if n%i == 0:
                    factors.append(i)
            except ZeroDivisionError:
                continue
    else:
        for i in range(-n,n,-1):
            try:
                if n%i == 0:
                    factors.append(i)
            except ZeroDivisionError:
                continue
    factors.append(n)
    return factors

print(sorted(find_factors(5045)))