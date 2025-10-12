import math

def all_minimal_diffs(nums: list[int]) -> list[list[int]]:
    min_diff = math.inf
    list_of_pairs = []
    nums.sort()
    for index in range(1, len(nums)):
        current_diff = nums[index] - nums[index - 1]
        current_pair = [nums[index - 1], nums[index]]
        if current_diff < min_diff:
            min_diff = current_diff
            list_of_pairs = [current_pair]
        elif current_diff == min_diff:
            list_of_pairs.append(current_pair)
        else:
            continue


    return list_of_pairs

def all_minimal_diffs_yt(nums: list[int]):
    min_diff = math.inf
    list_of_pairs = []
    nums.sort()
    for index in range(1, len(nums)):
        min_diff = min(min_diff, nums[index] - nums[index - 1])

    for index in range(1, len(nums)):
        if nums[index] - nums[index - 1] == min_diff:
            list_of_pairs.append([nums[index - 1], nums[index]])

    return list_of_pairs


if __name__ == '__main__':
    print(all_minimal_diffs([4, 2, 1, 3]))
    print(all_minimal_diffs([1, 3, 6, 10, 15]))
    print(all_minimal_diffs([3, 8, -10, 23, 19, -4, -14, 27]))
    print(all_minimal_diffs_yt([4, 2, 1, 3]))
    print(all_minimal_diffs_yt([1, 3, 6, 10, 15]))
    print(all_minimal_diffs_yt([3, 8, -10, 23, 19, -4, -14, 27]))

