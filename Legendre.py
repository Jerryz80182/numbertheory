import math
sqrt = math.sqrt

def sieve(n):
    '''wheel sieve with modulo 30.'''
    if not (type(n) == type(int())):
        raise TypeError
    if n < 0:
        raise ValueError
    if n < 2:
        return []
    prime = [True for x in range(2, n+1)]
    primes = []
    i = 0
    s = int(sqrt(n)-1)
    while i < n-1:
        if prime[i] == True:
            primes.append(i+2)
            if i < s:
                index = (i+2)**2 - 2
                while index < n-1:
                    prime[index] = False
                    index = index + i + 2
        if i > 4:
            if i > 28:
                if (i + 2)%30 == 1:
                    i = i + 6
                elif (i + 2)%30 == 7:
                    i = i + 4
                elif (i + 2)%30 == 11:
                    i = i + 2
                elif (i + 2)%30 == 13:
                    i = i + 4
                elif (i + 2)%30 == 17:
                    i = i + 2
                elif (i + 2)%30 == 19:
                    i = i + 4
                elif (i + 2)%30 == 23:
                    i = i + 6
                elif (i + 2)%30 == 29:
                    i = i + 2
            else:
                if (i + 2)%6 == 1:
                    i = i + 4
                elif (i + 2)%6 == 5:
                    i = i + 2
        else:
            i = i + 1
    return primes

def prime_test(n):
    '''A naïve deterministic primality test.'''
    if not (type(n) == type(int())):
        raise TypeError
    if not (n > 1):
        raise ValueError
    for prime in sieve(sqrt(n)):
        if n%prime == 0:
            return False
    return True

def Legendre(a, p):
    '''computes the Legendre symbol (a/p).'''
    if not ((type(a) == type(int())) and (type(p) == type(int()))):
        raise TypeError
    if not (p > 2):
        raise ValueError
    if not prime_test(p):
        raise ValueError
    return (a**((p-1)//2))%p
