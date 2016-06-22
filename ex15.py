from sys import argv
# stores the name of the file in variable filename
#script, filename = argv

# opens and creates an object of the file
#txt = open(filename)
print "Write the name of your file:"
filename = raw_input('--> ')

# prints the name of the file 
print "Here's your file %r:" % filename

txt = open(filename)

# reads the object created 
print txt.read()

txt.close()

