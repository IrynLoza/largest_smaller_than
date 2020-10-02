"""Return index of largest num in sorted list that is smaller than given num.

For example:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    1

If no such number exists, return True:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10)
    True

"""


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number.
    [-5, -2, 8, 12, 32], 10"""
    new = []
    for num in nums:
        if num < xnumber:
            new.append(num)  
     
    if new:  
        target = new[0] 
        for el in new:
            if el > target:
                target = el
        return new.index(target)
    else:
        return True          


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. YOU ARE THE MAXIMUM!\n")

         


