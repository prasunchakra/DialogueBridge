"""
01: Variable argument functions
02: Keyword-only argument functions
"""
def keyArgs(arg1, arg2, *, suppressExceptions=False):
    """
    Demonstrate the use of keyword-only arguments
    """
    print(arg1, arg2, suppressExceptions)

def varArgs(base, *args):
    """
    Demonstrate the use of variable argument lists
    """
    print(base)
    result = 0
    for arg in args:
        result += arg

    return result


def main():
    # pass different arguments
    print(varArgs("BASE", 10, 15, 20))
    print(varArgs(1, 2, 3))

    # pass an existing list
    myNums = [5, 10, 15, 20]
    print(varArgs("HI",*myNums))

    # try to call the function without the keyword
    # myFunction(1, 2, True)
    keyArgs(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
