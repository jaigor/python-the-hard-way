from sys import argv

print "Choose your file to read: "
filename = raw_input('> ')

targetR = open(filename, 'r') # here the file is opened for reading

print targetR.read()

print "Do you want to add something to %s?" % filename
print "If don't, hit CTRL-C (^C)." # used to exit the prompt
print "If yes, hit RETURN." # you can put anything, RETURN does the work
targetR.close()

raw_input('> ')
# the file is opened for writing (append), that means is adding text with the old one
targetW = open(filename, 'a') 

print "Write your sentence: "
sentence = raw_input('> ')

targetW.write(sentence)

targetW.close()