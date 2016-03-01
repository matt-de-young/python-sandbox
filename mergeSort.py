import random
import linkedList

def merge_sort(list):
    if list.length < 2:
        return list

    # Divide the list down the middle
    left = linkedList.LinkedList()
    right = linkedList.LinkedList()
    for num in range(0, list.length):
        if num % 2 == 0:
            right.add(list.remove())
        else:
            left.add(list.remove())

    # Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)

    # Then merge the now-sorted sublists.
    return merge(left, right)

def merge(left, right):
    result = linkedList.LinkedList()

    # put smaller from each list in front
    while left.length>0 and right.length>0:
        if left.first.data <= right.first.data:
            result.add(left.remove())
        else:
            result.add(right.remove())

    # Add what's left
    while left.length > 0:
        result.add(left.remove())
    while right.length > 0:
        result.add(right.remove())
    return result