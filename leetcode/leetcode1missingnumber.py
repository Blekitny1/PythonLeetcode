# This is a sample Python script.

def missing_number(nums: list[int]):
    n = len(nums)
    full_nums = {i for i in range(n + 1)}
    return list(full_nums.difference(set(nums)))[0]

def missing_number_yt(nums: list[int]):
    4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(missing_number([1, 2, 0, 4, 5, 3]))
    print(missing_number([1, 2, 3, 4]))
    print(missing_number([1, 2, 3, 4, 6, 0, 7, 8]))
    print(missing_number_yt([1, 2, 0, 4, 3]))
    print(missing_number_yt([1, 2, 3, 4]))
    print(missing_number_yt([1, 2, 3, 4, 6, 0, 7, 8]))


