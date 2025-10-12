def longest_mountain_in_array(nums: list[int]) -> int:
    longest_mountain = 0

    is_zero_down = nums[0] < nums[1]
    is_len_nums_down = nums[len(nums) - 2] > nums[len(nums) - 1]
    indexes_of_local_minimums = [i for i in range(1, len(nums) - 1) if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]]
    all_indexes_of_local_minimums = [0]*is_zero_down + indexes_of_local_minimums + [len(nums) - 1]*is_len_nums_down

    if len(all_indexes_of_local_minimums) < 2:
        return longest_mountain
    else:
        for index, value in enumerate(all_indexes_of_local_minimums):
            if index == 0:
                continue
            else:
                longest_mountain = max(longest_mountain, value - all_indexes_of_local_minimums[index - 1] + 1)

    return longest_mountain

def longest_mountain_in_array_yt(nums: list[int]):
    result = 0
    for i in range(1, len(nums) - 1):
        if nums[i -1] < nums[i] > nums[i + 1]:
            l = r = i
            while l >= 0  and nums[l] > nums[l - 1]:
                l -= 1
            while r < len(nums) - 1 and nums[r] > nums[r + 1]:
                r += 1
            result = max(result, r - l + 1)

    return result


if __name__ == '__main__':
    print(longest_mountain_in_array([7, 1, 5, 3, 6, 4]))
    print(longest_mountain_in_array([1, 7, 15, 24, 16, 12, 13]))
    print(longest_mountain_in_array([1, 2, 0, 3, -1, -4]))
    print(longest_mountain_in_array([2, 2, 2]))
    print(longest_mountain_in_array_yt([7, 1, 5, 3, 6, 4]))
    print(longest_mountain_in_array_yt([1, 7, 15, 24, 16, 12, 13]))
    print(longest_mountain_in_array_yt([1, 2, 0, 3, -1, -4]))
    print(longest_mountain_in_array_yt([2, 2, 2]))

