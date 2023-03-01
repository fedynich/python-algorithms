"""
In this problem, you have to implement the find_sum(arr,k)
Take a number k as input and return two numbers that add up to k.

Input:  A list and a number k
Output: A list with two integers a and b that add up to k

Example:
    arr = [1,21,3,14,5,60,7,6]
    k = 81

    return [21,60]
"""


def bruteforce(arr, sum):
    """
    Use nested loop
    O(n*n)
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                return [arr[i], arr[j]]

    return None


def hash(arr, sum):
    """
    Best solution

    O(1)
    """
    map = {}

    """
    For each element in the array:
        Calculate the complement by subtracting the current list element from the given number.
        Look up the complement in the hash table. If it exists, a pair that sums up to the given number has been found.
        Insert the current element of the array into the hash table after you perform the step above."""

    for i in range(len(arr)):
        complementary = sum - arr[i]

        if complementary in map:
            return [complementary, arr[i]]

        map[arr[i]] = arr[i]

    return None
