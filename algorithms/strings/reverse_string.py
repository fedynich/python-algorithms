"""
Example:
    Given string = "Hello World"

    return in reversed order: "dlroW olleH"
"""


def pythonic(s):
    """
    The best solution
    Reverse by slicing
    """
    return s[::-1]


def built_in_reversed(s):
    """
    Using reversed() method
    """

    return "".join(reversed(s))


def built_in_reverse(s):
    """
    Using list reverse() method
    """

    s = list(s)
    s.reverse()

    return "".join(s)


def iterative(s):
    """
    Classic backward loop iterations
    """

    result = ""

    for i in range(len(s), 0, -1):
        result += s[i - 1]

    return result


def list_comprehension(s):
    """
    Classic backward loop iterations in one line
    """

    return "".join([s[i - 1] for i in range(len(s), 0, -1)])


def recursive(s):
    """
    Recursive slicing last element and adding to the beginning
    """

    if not s:
        return s

    return s[-1] + recursive(s[:-1])


def stack(s):
    pass
