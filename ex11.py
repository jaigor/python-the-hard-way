print "How old are you?",
age = raw_input('--> ')
print "How tall are you?",
height = raw_input('--> ')
print "How much do you weigh?",
weight = raw_input('-->' )

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

print "Insert first number to add",
num1 = int(raw_input('--> '))
print "Insert second number to add",
num2 = int(raw_input('--> '))
addition = num1 + num2
print "Result %r" % addition 