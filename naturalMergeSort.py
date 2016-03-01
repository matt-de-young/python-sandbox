import linkedList

def natural_merge_sort(list):
    if list.length < 2:
        return list

    # Check for ascending runs
    run = linkedList.LinkedList()
    run.add(list.remove())

    while list.length > 0 and run.last.data <= list.first.data:
        run.add(list.remove())

    if run.length < 2:
        while list.length > 0 and run.first.data > list.first.data:
            run.push(list.remove())

    # Sort remainder
    rlist = natural_merge_sort(list)

    # Then merge the now-sorted sublists.
    return merge(run, rlist)

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