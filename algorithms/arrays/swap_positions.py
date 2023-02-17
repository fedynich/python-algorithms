"""
Given an array of elements, swap two 2nd and 5th elements

Example:
    Given array = [2, 7, 11, 15], pos1=2, pos2=5

    return [2, 15, 11, 7]
"""


def swap_positions_v2(array, pos1, pos2):
    """
    The best way

    Simple swap, using comma assignment

    Time Complexity: O(1), for using constant operations
    """
    array[pos1], array[pos2] = array[pos2], array[pos1]

    return array


def swap_positions_v1(array, pos1, pos2):
    """
    Using temp variable

    Time Complexity: O(1), for using constant operations.
    """

    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

    return array


def swap_positions_v3(array, pos1, pos2):
    """
    Using tuple variable

    Time Complexity: O(1), for using constant operations
    """

    get = array[pos1], array[pos2]
    array[pos2], array[pos1] = get

    return array
