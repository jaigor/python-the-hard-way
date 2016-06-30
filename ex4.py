# int number 100 on cars variable
cars = 100
# float number 4.0 on space...
space_in_a_car = 4.0
# int 30 on drivers
drivers = 30
# int 90 on passengers
passengers = 90
# substraction of the content in variables: 100 - 30 
cars_not_driven = cars - drivers
# get the content of drivers and set on cars_driven
cars_driven = drivers
# 30 * 4.0
carpool_capacity = cars_driven * space_in_a_car
# 90 / 30
average_passengers_per_car = passengers / cars_driven

# prints There are 100 cars available.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."