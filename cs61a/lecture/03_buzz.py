"""
This is the python implementation of buzz game.

It's based on the CS61a lecture on functional programming 2

This module supplies two functions, is_in_string() and buzz()
"""


def is_in_string(char, string):
    """Check for char occurence in provided string

    >>> is_in_string('3', str(15))
    False
    >>> is_in_string('5', str(15))
    True
    """
    for i in range(0, len(string)):
        if string[i] == char:
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
    print("buzz") if is_in_string("7", str(x)) or x % 7 == 0 else print(x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
