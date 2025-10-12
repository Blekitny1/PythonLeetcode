def find_missing_numbers(nums: list[int]):
    n = len(nums)
    full_list = [i for i in range(1, n + 1)]
    for num in nums:
        if num in full_list:
            full_list.remove(num)
    return full_list


def find_missing_numbers_2(nums: list[int]):
    n = len(nums)
    full_set_of_nums = set([i for i in range(1, n + 1)])
    return list(full_set_of_nums - set(nums))


if __name__ == '__main__':
    print(find_missing_numbers([1, 1]))
    print(find_missing_numbers([6, 2, 3, 4, 4, 2, 1, 8]))
    print(find_missing_numbers_2([1, 1]))
    print(find_missing_numbers_2([6, 2, 3, 4, 4, 2, 1, 8]))
