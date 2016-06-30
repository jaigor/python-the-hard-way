numbers = []

def while_num (var, counter):
	i = 0
	global numbers
	
	while i < var:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + counter
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

while_num(6,1)

print "The numbers: "

for num in numbers:
	print num