# well, first of all, the joke talks about the number 2 in binary
# yeah, I know that kun fu
# here declares different variables with strings
# inside them
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 2 strings inside

# and print them beacuse y has binary and do_not refered
print x
print y

# another way to do it
print "I said: %r." % x
print "I also said: '%s'." % y # and other two x and y

hilarious = False
# joke has declared inside the string 
# a format character...
joke_evaluation = "Isn't that joke so funny?! %r"

# ...making printed here the content of hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# this is a chain or array of strings
print w + e
