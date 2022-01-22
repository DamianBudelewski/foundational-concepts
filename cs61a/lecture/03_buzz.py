"""
This is the python implementation of buzz game.

It's based on the CS61a lecture on functional programming 2

This module supplies two functions, in_string() and buzz()
"""


def in_string(string, value):
    """Check for number occurence in provided string

    >>> in_string(str(15),'3')
    False
    >>> in_string(str(15),'5')
    True
    """
    for i in range(0, len(string)):
        if string[i] == value:
            return True
    return False


def buzz(x):
    """Print 'buzz' when x is a multiple of 7 or is a number with a 7 in it

    >>> buzz(4)
    4
    >>> buzz(7)
    buzz
    >>> buzz(14)
    buzz
    >>> buzz(17)
    buzz
    >>> buzz(20)
    20
    """
    print("buzz") if in_string(str(x), "7") or x % 7 == 0 else print(x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
