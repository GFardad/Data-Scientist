import random


def stepone(n):

    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    else:
        return stepthree(n, 50)


def steptwe(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
            a = a**2 % m
            b = b // 2
    return result


def seteo(n):
    nq = n - 1
    e, o = 0, nq
    while o % 2 == 0:
        o = o // 2
        e += 1
    return e, o


def inputu():
    n = int(input("Test is X a Prime number? : "))
    return n


def main():
    stepone(inputu())


def stepthree(n, k):

    for kon in range(0, k):
        e, d = seteo(n)
        ran = random.randint(2, n - 2)
        r = steptwe(ran, d, n)


main()
