"""
01: List Comprehension
02: Dictionary Comprehension
03: Set Comprehension
"""

def SetComprehensions():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a set of unique Fahrenheit temperatures
    ftemps1 = [(t * 9/5) + 32 for t in ctemps]
    ftemps2 = {(t * 9/5) + 32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)

    # build a set from an input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)

def DictComprehensions():
    """
    Demonstrate how to use dictionary comprehensions
    """
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    tempDict = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)

def ListComprehensions():
    """
    Demonstrate how to use list comprehensions
    """
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Perform a mapping and filter function on a list
    evenSquared = list(
        map(lambda e: e**2, filter(lambda e: e > 4 and e < 16, evens)))
    print(evenSquared)

    # Derive a new list of numbers frm a given list
    evenSquared = [e ** 2 for e in evens]
    print(evenSquared)

    # Limit the items operated on with a predicate condition
    oddSquared = [e ** 2 for e in odds if e > 3 and e < 17]
    print(oddSquared)

def main(options):
    if options == 1:
        ListComprehensions()
    elif options == 2:
        DictComprehensions()
    elif options == 3:
        SetComprehensions()
if __name__ == "__main__":
    main()