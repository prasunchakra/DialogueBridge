"""
01: List Functions
02: Iterators
03: Transformers
TODO: itertools (built in library)
"""

def iterators():
    """
     use of iterator functions like enumerate, zip, iter, next
    """
    # define a list of days in English and French
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    daysBn = ["Shom", "Mongol", "Budh", "Brihoshpoti", "Shukro", "Shoni", "Robi"]

    # use iter to create an iterator over a collection.
    # Get an iterator from an object.
    # In the first form, the argument must supply its own iterator, or be a sequence.
    # In the second form, the callable is called until it returns the sentinel.
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # iterate using a function and a sentinel
    with open("01_BasicCodingStyle.py", "r") as fp:
        for line in iter(fp.readline, 'class'):
            print(line)

    # use regular interation over the days
    for m in range(len(days)):
        print(m+1, days[m])

    # using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    for m in zip(days, daysBn):
        print(m)

    for i, m in enumerate(zip(days, daysBn), start=1):
        print(i, m[0], "=", m[1], "in Bengali")


def listFunction():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values are true
    print(any(list1))
    
    # all will return true only if all values are true
    print(all(list1))
    
    # min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1))
    print("max: ", max(list1))    
    
    # Use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1))
def transformers():
    """
    use transform functions like sorted, filter, map
    """
    def toGrade(x):
        if (x >= 90):
            return "A"
        elif (x >= 80 and x < 90):
            return "B"
        elif (x >= 70 and x < 80):
            return "C"
        elif (x >= 65 and x < 70):
            return "D"
        return "F"
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    odds = list(filter(lambda x: False if x%2==0 else True, nums))
    print(odds)

    # use filter on non-numeric sequence
    lowers = list(filter(lambda x: False if x.isupper() else True , chars))
    print(lowers)

    # use map to create a new sequence of values
    squares = list(map(lambda x: x**2, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)
    
    
if __name__ == "__main__":
    # listFunction()
    # iterators()
    transformers()