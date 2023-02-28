"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
Name it merge_lists(lst1, lst2).

Input:  Two sorted lists.
Output: A merged and sorted list consisting of all elements of both input lists

Example:
    list1 = [1,3,4,5]
    list2 = [2,6,7,8]

    return [1,2,3,4,5,6,7,8]
"""


def generate_new_array(arr1, arr2):
    """
    Time Complexity: O(n + m) where n and mare the lengths of the lists
    """

    result = []
    i, j = 0, 0

    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append whatever is left of list2 or list1
    if i == len(arr1) and j < len(arr2):
        result.extend(arr2[j:])
    else:
        result.extend(arr1[i:])

    return result


def merge_in_place(arr1, arr2):
    """
    Time Complexity: O(n + m) where n and mare the lengths of the lists
    """

    i, j = 0, 0

    # If the current element of list1 is greater
    # than the current element of list2
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            # insert list2's current index to list1
            arr1.insert(i, arr2[j])
            i += 1
            j += 1
        else:
            i += 1

    # Append whatever is left of list2 to list1
    if j < len(arr2):
        arr1.extend(arr2[j:])

    return arr1