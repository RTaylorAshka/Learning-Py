def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    nslice = slice(3)

    while len(nums) >= 3:
        # print(nums[nslice])

        if sum(nums[nslice]) % 2 != 0:
            return True

        nums.pop(0)

    return False
