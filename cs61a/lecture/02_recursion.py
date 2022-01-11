"""Task: calculate the sum of the positive integers of n+(n-2)+(n-4)...

Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""


def sum_series(n):
    """Calculate sum of n+(n-2)+(n-4)..."""
    return n if n < 2 else n + sum_series(n - 2)
