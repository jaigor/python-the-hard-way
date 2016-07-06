from exceptions import ValueError

# Keywords
if 1 == 1:
	assert True, "Not an Error!"
else:
	assert False, "Error on maths"

cont = 1
while True:
	if cont > 5:
		print "Stop, cont is %d" % cont
		break # stops execution
	cont += 1

	if cont > 2:
		print "cont is higher than 2"
		continue # continues with the loop but moves the control back to the top of the loop
	print "cont is %d" % cont # this statement is not executed when cont is > 2

list_item = ['a','b','c']
del list_item[2]
print list_item

def global_var():
	global varGlobal 
	varGlobal = "function1"
	varLocal = "function2"

global_var()
print varGlobal
# print varLocal == Error

# lambda = anonymous functions http://www.secnetix.de/olli/Python/lambda_functions.hawk
def f (x): return x**2

print f(8)

g = lambda x: x**2
print g(8) #same result

# yield = returns value but keeps the iterator frozen  https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

def simple_generator_function():
	yield 1
	yield 2
	yield 3

for value in simple_generator_function():
	print(value)

our_generator = simple_generator_function()
print next(our_generator)
print next(our_generator)
print next(our_generator) # same result, until next is called keeps the order on the iterator

# pass = acts as a placeholder (null), example a class with methods to define later
class MyClass(object):
	def meth_a(self):
		pass

	def meth_b(self):
		print "I'm meth_b"
# exec = compiles and evaluates an string or an object
exec("print('so this works like eval')")

exec("list_str = [2,5,6,7,3]")
print (list_str)

exec("""
def test():
	print('lets call this function')
""")

test()

# handling exceptions
# try, except, finally, raise
(x,y) = (5,0)
try:
	z = x/y
except ZeroDivisionError:
	print "divided by zero"
finally:
	print "execute this!"

while True:
	try:
		inputVar = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops! That was no valid number. Try again...")
		if not can_handle(e):
			raise # makes the exception raises (debugger tool)
		handle_exception(e)
	finally:
		print "Execute this always"

# with, as: assigned to a variable with "as", for example to
# open a file, that always is going to close after execution of http  code://effbot.org/zone/python-with-statement.htm
with open("x.txt") as f:
    data = f.read()
    do something with data

# Data Types
print "\n"
x = None
print x

tof = True or False
fat = False and True
print tof
print fat

i = 150
f = 34.50
sumatory = i + f # automatically sumatory inializes like a float
print sumatory

# dicts (similar hashmap)
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print (a == b == c == d == e)

dicts = {'a': 1, 'b': 2, 'c': 3}
print ('a' in dicts) # True
print dicts.items()
for i in dicts: # only keys
	print i

for i in dicts.iteritems(): # keys and values
	print i

# String Escape Sequences
print "\n"
print "Hola, esto es un \\ perro"
print "Hola, \'esto\' es un \"perro\""
print "Hola, esto es un perro\b verde" # \a = bell, sound
print "Hola, esto es un \f perr \r o"
print "Hola, \testo es un \v perro"

# String Formats
print "\n"
print "%d" % 45 
print "%i" % 45 
print "%o" % 1000 # octal number
print "%x" % 1000 # hexadecimals
print "%X" % 1000
print "%e" % 1000 # Exponential notation
print "%f" % 10.34 # float large
print "%g" % 10.34 # float shorter
print "%r" % int # repr format (debugging)

# Operators
print "\n"
print 2 ** 4 # power of (potencia)
print 2 // 4.0 # floor division, division round by negative 
# @ At (decorators) http://thecodeship.com/patterns/guide-to-python-function-decorators/
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate # same as:
#				my_get_text = p_decorate(get_text)
#				print my_get_text("John")
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")

# assigments
var = 1

var += 2
print var

var -= 2
print var

var *= 2
print var

var /= 2
print var

var = 15
var //= 2
print var

var %= 2
print var

var **= 2
print var