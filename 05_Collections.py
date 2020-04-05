"""
The Collection Objects
01: namedtuple
02: defaultdict
03: Counter
04: OrderedDict
05: deque
"""

import collections
import string

def Deque():
    """
    deque (pronounced as deck) objects are like double-ended queues
    """
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    d.rotate(1)
    print(d)
def OrderedDict():
    """
    Demonstrate the usage of OrderedDict objects
    """
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = collections.OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = collections.OrderedDict({"a": 1, "b": 2, "c": 3})
    b = collections.OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)


def Counter():
    """
    Demonstrate the usage of Counter objects
    """
    # list of students in class 1
    class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for class1 and class2
    c1 = collections.Counter(class1)
    c2 = collections.Counter(class2)

    # How many students in class 1 named James?
    print(c1["James"])

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)

def DefaultDict():
    """
    Demonstrate the usage of defaultdict objects
    """
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = collections.defaultdict(int)
    
    # Count the elements in the list, normal dict would give key not found error.
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


def NamedTuples():
    """
    Demonstrate the usage of namdtuple objects
    """

    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)
    print(p2[0],p2[1])
    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    # 'Point' object does not support item assignment
    # p2[1]=300 
    print(p1)


def main(options):
    if options==1:
        NamedTuples()
    elif options ==2:
        DefaultDict()
    elif options ==3:
        Counter()
    elif options ==4:
        OrderedDict()
    elif options ==5:
        Deque()
if __name__ == "__main__":
    main(5)