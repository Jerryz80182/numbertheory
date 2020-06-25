#print out all 1 to (input - 1) square mod input  
def quad(input):
	l = []
	for i in range(1,input):
		output = (i**2) % input
		l.append(output)
	print(l)

#print out the possible elements match in totient(input) which their products mod input is 1
def match_to_one(input):
	list = [] 
	for i in range(2,input-1):
		list.append(i)
    	output = [(x, y) for x in list for y in list if (x * y) % input == 1]
    	print(set(output))

#print all the possible outcomes of quadratic of elements in totient(input)
def quad_possibleoutcomes(input):
	l = []
	for i in range(1,input):
		outcome = (i**2) % input
	 	l.append(outcome)
	print(set(l))







