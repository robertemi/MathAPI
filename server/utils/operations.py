def factorial(number):
    return 1 if number <= 1 else number * factorial(number - 1)


def fibbonaci(number):
    a = 0
    b = 1
    i = 1

    while i < number:
        c = a + b
        a = b
        b = c
        i += 1

    return c


def power(base, exponent):
    result = 1

    for i in range(abs(exponent)):
        result = result * base

    if exponent < 0:
        return 1 / result
    else:
        return result
