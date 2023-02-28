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

    if i == len(arr1) and j < len(arr2):
        result.extend(arr2[j:])
    else:
        result.extend(arr1[i:])

    return result
