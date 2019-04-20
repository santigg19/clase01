"""def factorial (number):
    t=1
    for n in range(number):
        t = t*(n+1)


    return t """

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)