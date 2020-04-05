"""
Advanced Classes
01: enum
02: Customizing String Representation of Objects 
    01: __repr__, __str__, __bytes__
    02: __getattr__, __setattr__, __dir__
03: Customizing Numeric Representation of Objects 
    01: objects number-like behavior
    02: numerically compare objects to each other
"""

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person Class - fname:{0}, lname:{1}, age{2}>".format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return "Person ({0} {1} is {2})".format(self.fname, self.lname, self.age)

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ("rgbolor", "hexcolor")

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level

def NumObj(options):
    """
    give objects number-like behavior
    """
    if options == 1:
        p1 = Point(10, 20)
        p2 = Point(30, 30)
        print(p1, p2)

        # Add two points
        p3 = p1 + p2
        print(p3)

        # subtract two points
        p4 = p2 - p1
        print(p4)

        # Perform in-place addition
        p1 += p2
        print(p1)
    elif options ==2:
        # define some employees
        dept = []
        dept.append(Employee("Tim", "Sims", 5, 9))
        dept.append(Employee("John", "Doe", 4, 12))
        dept.append(Employee("Jane", "Smith", 6, 6))
        dept.append(Employee("Rebecca", "Robinson", 5, 13))
        dept.append(Employee("Tyler", "Durden", 5, 12))

        # Who's more senior?
        print(bool(dept[0] > dept[2]))
        print(bool(dept[4] < dept[3]))

        # sort the items
        emps = sorted(dept)
        for emp in emps:
            print(emp.lname)


def StrObj(options):
    """
    customize string representations of objects
    """
    if options == 1:

        # create a new Person object
        cls1 = Person()

        # use different Python functions to convert it to a string
        print(repr(cls1))
        print(str(cls1))
        print("Formatted: {0}".format(cls1))
        print(bytes(cls1))
    elif options == 2:
         # create an instance of myColor
        cls1 = myColor()
        # print the value of a computed attribute
        print(cls1.rgbcolor)
        print(cls1.hexcolor)

        # set the value of a computed attribute
        cls1.rgbcolor = (125, 200, 86)
        print(cls1.rgbcolor)
        print(cls1.hexcolor)

        # access a regular attribute
        print(cls1.red)

        # list the available attributes
        print(dir(cls1))

def Enumerations():
    """
    define enumerations using the Enum base class
    enums have human-readable values and types
    """
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])

def main(option):
    if option == 1:
        Enumerations()
    if option == 2:
        StrObj(2)
    if option == 3:
        NumObj(2)

if __name__ == "__main__":
    main(3)