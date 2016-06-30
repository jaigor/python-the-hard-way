# definition of a function that has two parameters and
# the rest of sentences that print their values adding strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# calling function with only numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# calling function with variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calling function with maths
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calling function with maths and variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def print_file(filename):
	in_file = open(filename)
	data = in_file.read()
	print "The file contains: \n %r" % data
	in_file.close()

print "Insert the name of the file: "
filename = raw_input('> ')

print_file(filename)