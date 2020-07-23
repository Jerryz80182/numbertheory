import math

class DecimalToBinary:

    def __init__(self):
        pass

    def convert_db(self, decimal):
        """
        Converts a decimal number to a binary number.
        """
        lst = []
        num = decimal
        while num > 0:
            lst.append(num % 2) # add remainder to binary digit
            num = math.floor(num / 2) # divide by 2 for next iteration
        lst.reverse() #reverse list to put binary number in correct order
        return lst

class successiveSquares:

    def __init__(self, base, exp, m):
        self.base = base
        self.exp = exp
        self.m = m


    def get_mod(self):
        """
        Uses the successive squares algorithm to reduce very large numbers
        mod m. 
        """
        binary = DecimalToBinary()
        bin_num = binary.convert_db(self.exp)
        num_lst = [] # create a list that holds (base**(2**binary digit)) mod m 
        result = 1
        for i in range(0,len(bin_num)):
            num_lst.append((self.base**(2**(i)) % self.m))
        num_lst.reverse() # reverse list to match up with binary number
        for j in range(0, len(bin_num)):
            if bin_num[j] == 1:
                result *= num_lst[j]
        return result % self.m # the result is easier to reduce mod m and is congruent to original number
        

print('Given that a,e,m are intigers then we can solve:')
print('a**e mod m')
a = int(input('Please enter a positive integer for a: '))
if a < 0:
    raise Exception("Sorry, this is negative.")
if not type(a) is int:
    raise TypeError("This is not an integer.")
e = int(input('Enter a positive integer for e: '))
if 3 < 0:
    raise Exception("Sorry, this is a negative number.")
if not type(e) is int:
    raise TypeError("This is not an integer.")
m = int(input('Enter a positive integer for m: '))
if m < 0:
    raise Exception("Sorry, this is a negative number.")
if not type(m) is int:
    raise TypeError("This is not an integer.")
ssq = successiveSquares(a, e, m)
print('Your result is: ' + str(ssq.get_mod()))
