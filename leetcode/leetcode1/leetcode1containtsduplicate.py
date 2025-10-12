def contains_duplicate(nums: list[int]):
    if len(nums) < 2:
        return False
    else:
        previous_values = set()
        for num in nums:
            if num in previous_values:
                return True
            else:
                previous_values.add(num)
        return False


def contains_duplicate_yt(nums: list[int]):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True



if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 4, 3]))
    print(contains_duplicate([1, 2, 3, 4, 6]))
    print(contains_duplicate([1, 2, 3, 4, 6, 6756, 23, 565, 232, 3]))
    print(contains_duplicate_yt([1,2,3,4,3]))
    print(contains_duplicate_yt([1,2,3,4,6]))
    print(contains_duplicate_yt([1,2,3,4,6,6756,23,565,232,3]))

