import math

#is x**2 congruent to a mod m?
#returns number if found, else returns 0
def compute_square(a, m):
    #make sure that a is within the totient set of m
    if a > m:
        a = a % m
    found = 0
    #only need to find squares up to floor(m / 2), because x**2 = (-x)**2
    for x in range (1, math.floor(m / 2)):
        if(x**2) % m == a:
            found = x
    return found

print('This checks for quadratic residues in the form:')
print('x**2 congruent to a mod m')
a = int(input('Please enter a positive integer for a: '))
#check condition of input to ensure that it is correct
if a < 0:
    raise Exception("Sorry, this is negative.")
if not type(a) is int:
    raise TypeError("This is not an integer.")
m = int(input('Now enter a positive integer for m: '))
#check condition of input to ensure it is correct
if m < 0:
    raise Exception("Sorry, this is a negative number.")
if not type(m) is int:
    raise TypeError("This is not an integer.")

result = compute_square(a,m)
if result != 0:
    print("quadratic residue found: " + str(result))
else:
    print('This is a quadratic non-residue')
