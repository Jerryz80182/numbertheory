# Takes the product of all of the elements in a list
def prod(l):
    if not (type(l) == type(list())):
        raise TypeError
    p = 1
    for n in l:
        if not ((type(n) == type(int())) or (type(n) == type(float()))):
            raise TypeError
        p = p*n
    return p

# Finds the determinant ad-bc of a matrix [[a, b], [c, d]]
def det(mat):
    if not (type(mat) == type(list())):
        raise TypeError
    if not (len(mat) == 2):
        raise ValueError
    if not (type(mat[0]) == type(list())):
        raise TypeError
    if not (len(mat[0]) == 2):
        raise TypeError
    if not (type(mat[0][0]) == type(int())):
        raise TypeError
    if not (type(mat[0][1]) == type(int())):
        raise TypeError
    if not (type(mat[1]) == type(list())):
        raise TypeError
    if not (len(mat[1]) == 2):
        raise TypeError
    if not (type(mat[1][0]) == type(int())):
        raise TypeError
    if not (type(mat[1][1]) == type(int())):
        raise TypeError
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

# Implements the Euclidean Algorithm for two numbers, a and b
def EuclidAlg(a, b):
    if not (type(a) == type(int())):
        raise TypeError
    if not (type(b) == type(int())):
        raise TypeError
    if not (a > 0):
        raise ValueError
    if not (b > 0):
        raise ValueError
    if (a%b == 0):
        return str(a) + ' = ' + str(b) + '•' + str(a//b) + ' + ' + str(a%b)
    return str(a) + ' = ' + str(b) + '•' + str(a//b) + ' + ' + str(a%b) + '\n' + EuclidAlg(b, a%b)

# Finds the gcd of two numbers, a and b
def gcd(a, b):
    if not (type(a) == type(int())):
        raise TypeError
    if not (type(b) == type(int())):
        raise TypeError
    if not (a > 0):
        raise ValueError
    if not (b > 0):
        raise ValueError
    if (a < b):
        return gcd(b, a)
    if (a%b == 0):
        return b
    return gcd(b, a%b)

# Implements the Magic Table for the numbers a and b
def MagicTbl(a, b):
    if not (type(a) == type(int())):
        raise TypeError
    if not (type(b) == type(int())):
        raise TypeError
    if not (a > 0):
        raise ValueError
    if not (b > 0):
        raise ValueError
    if (a%b == 0):
        raise ValueError
    quotients = []
    x = a
    y = b
    while x%y != 0:
        quotients.append(x//y)
        x, y = y, x%y
    results = [[None, None] + quotients, [1, 0], [0, 1]]
    for q in quotients:
        results[1].append(q * results[1][-1] + results[1][-2])
        results[2].append(q * results[2][-1] + results[2][-2])
    return results

# Solves the Bezout identity for the numbers a and b (in the form of a list [x, y] where ax + by = gcd(a, b))
def BezoutSol(a, b):
    MagTbl = MagicTbl(a,b)
    d = det([[MagTbl[1][-2], MagTbl[1][-1]], [MagTbl[2][-2], MagTbl[2][-1]]])
    return [MagTbl[1][-1] * -1 * d, MagTbl[2][-1] * d]

# Chinese Remainder Theorem solver
def CRT(values, mods, mode = 'no work'):
    if not (type(values) == type(list())):
        raise TypeError
    if not (type(mods) == type(list())):
        raise TypeError
    if not (type(mode == type(str()))):
        raise TypeError
    if not (len(values) > 0):
        raise ValueError
    if not (len(mods) > 0):
        raise ValueError
    if not (len(values) == len(mods)):
        raise ValueError
    if not (mode.lower() in ['showwork', 'show work', 'work', 'nowork', 'no work', 'solutiononly', 'solution only', 'solution']):
        raise ValueError
    N = prod(mods)
    if mode in ['showwork', 'show work', 'work']:
        print("N: ", N)
        print()
    k = len(values)
    x = 0
    for i in range(k):
        if mode in ['showwork', 'show work', 'work']:
            print("N_i:", N//mods[i])
            print("Euclid:")
            print(EuclidAlg(N//mods[i], mods[i]))
            print("Magic:")
            for m in MagicTbl(N//mods[i], mods[i]):
                print(m)
            print("Inverse mod n_i:")
            print(BezoutSol(N//mods[i], mods[i])[0])
        x = x + N//mods[i] * BezoutSol(N//mods[i], mods[i])[0] * values[i]
        if mode in ['showwork', 'show work', 'work']:
            print("x:", x)
            print()
    if mode in ['showwork', 'show work', 'work']:
        print("x mod N:", x%N)
    return x%N

prime = int(input("What is the prime you want to test for being a square mod some arbitrary prime p? "))
primes = [CRT([prime % 4, 0], [4, prime])]
for i in [1, 3]:
    for j in range(1, prime):
            primes.append(CRT([i, j], [4, prime]))
primes = sorted(primes)
squareprimes = [2]
for p in primes:
    if ((-1)**((p-1)//2)) * (((p**((prime - 1)//2) + 1) % prime) - 1) in [0, 1]:
        squareprimes.append(p)
squareprimes = sorted(squareprimes)
print(str(prime) + " is a square mod p if and only if p is equivalent to " + str(squareprimes[:-1])[1:-1] + ", or " + str(squareprimes[-1]) + " modulo " + str(4 * prime) + ".")
