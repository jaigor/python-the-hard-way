from sys import argv

script, surname, age = argv

name = raw_input("What's your name?")

print "Your name is %r %r and you are %r " % (name, surname, age)