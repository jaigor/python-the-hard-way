## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    stamina = 100
    skills = []
    
    def eat(self):
        self.stamina += 10

    def hunger(self):
        self.stamina -= 10
        if self.stamina <= 0:
            is_dead()

    def is_dead(self):
        print "Animal is dead"

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

## Dog is-a class of Animal (inheritance of Animal)
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute called name passed as a parameter
        self.name = name

    def bark(self):
        print "%r says Guau!" % self.name

    def scan_stamina(self):
        print "Stamina: %d" % self.stamina

## Cat is-a class of Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name...
        self.name = name
        self.add_skill("scratch")
        self.add_skill("claw")


pluto = Dog("Pluto")
pluto.bark()
pluto.scan_stamina()

pluto.hunger()
pluto.scan_stamina()

garfield = Cat("Garfield")
print garfield.skills

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a a name passed as a parameter
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a class of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## this method executes the constructor of Person passing name as a parameter
        super(Employee, self).__init__(name)
        ## Person has-a salary passed as a parameter
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a class of Fish (inheritance)
class Salmon(Fish):
    pass

## Halibut is-a class of Fish (inheritance)
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet called satan (assigned)
mary.pet = satan

## frank is-a Employee and has-a name called Frank and a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover (assigned)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()