"""
Implement a function that removes all the even elements from a given list.
Name it remove_even(lst).

Input:  A list og random integers
Output: A list with only odd integers

Example:
    Given array = [2, 7, 11, 15, 2, 6, 2, 15, 8]

    return [7, 11, 15, 15]
"""


def list_comprehension(lst):
    return [n for n in lst if n % 2 != 0]


def classic(lst):
    result = []

    for n in lst:
        if n % 2 != 0:
            result.append(n)

    return result
