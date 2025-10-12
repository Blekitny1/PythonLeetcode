import math


def max_subarray(nums: list[int]) -> int:
    if max(nums) <= 0:
        return max(nums)
    left_border, min_sum_left, right_border, min_sum_right, temp_sum = -1, 0, len(nums), 0, 0
    for i in range(len(nums)):
        temp_sum += nums[i]
        if temp_sum < min_sum_left:
            min_sum_left = temp_sum
            left_border = i

    temp_sum = 0
    for i in range(len(nums) - 1, 0, -1):
        temp_sum += nums[i]
        if temp_sum < min_sum_right:
            min_sum_right = temp_sum
            right_border = i

    return sum(nums[left_border + 1 : right_border])

def max_subarray_yt(nums: list[int]):
    max_sum = nums[0]
    current_sum = 0
    for num in nums:
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([5, 4, -1, 7, 8]))
    print(max_subarray([1]))
    print(max_subarray_yt([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_yt([5, 4, -1, 7, 8]))
    print(max_subarray_yt([1]))

