numbers = []

def while_num ():
	global numbers
	
	for i in range(0, 6):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

while_num()

print "The numbers: "

for num in numbers:
	print num