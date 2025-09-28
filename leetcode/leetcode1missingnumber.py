def missing_number(nums: list[int]):
    n = len(nums)
    full_nums = {i for i in range(n + 1)}
    return list(full_nums.difference(set(nums)))[0]


def missing_number_yt(nums: list[int]):
    return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    print(missing_number([1, 2, 0, 4, 5, 3]))
    print(missing_number([1, 2, 3, 4]))
    print(missing_number([1, 2, 3, 4, 6, 0, 7, 8]))
    print(missing_number_yt([1, 2, 0, 5, 4, 3]))
    print(missing_number_yt([1, 2, 3, 4]))
    print(missing_number_yt([1, 2, 3, 4, 6, 0, 7, 8]))


