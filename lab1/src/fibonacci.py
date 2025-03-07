def fibonacci(n):

    if  type(n) != int :
        raise ValueError
    if n < 0 :
        raise ValueError

    if n == 0:
        return 0
    n0=1
    n1=1
    for i in range(n - 1):
        n1 += n0
        n0 = n1 - n0
    return n0

print(fibonacci(10))