import math

def min_subarray_size(nums: list[int], target: int) -> int:
    result = math.inf
    i, j = 0, 1

    if len(nums) < 3:
        if max(nums) > target:
            return 1
        elif sum(nums) >= target:
            return 2
        else:
            return 0

    else:
        while j < len(nums):
            if sum(nums[i:j + 1]) >= target:
                result = min(result, j - i + 1)
                i += 1
            if sum(nums[i:j + 1]) < target:
                j += 1

    if result == math.inf:
        return 0
    return result

def min_subarray_size_yt(nums: list[int], target: int) -> int:
    left = 0
    result = math.inf
    total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1

    if result == math.inf:
        return 0

    return result

def min_subarray_size_nlogn(nums: list[int], target: int) -> int:
    nums.sort(reverse=True)
    for i in range(len(nums) - 1):
        if sum(nums[:i + 1]) >= target:
            return i + 1
    return 0


if __name__ == '__main__':
    print(min_subarray_size([2, 3, 1, 2, 4, 3], 7))
    print(min_subarray_size([1, 4, 4], 4))
    print(min_subarray_size([1, 1, 1, 1, 1, 1, 1], 11))
    print(min_subarray_size_yt([2, 3, 1, 2, 4, 3], 7))
    print(min_subarray_size_yt([1, 4, 4], 4))
    print(min_subarray_size_yt([1, 1, 1, 1, 1, 1, 1], 11))
    print(min_subarray_size_nlogn([2, 3, 1, 2, 4, 3], 7))
    print(min_subarray_size_nlogn([1, 4, 4], 4))
    print(min_subarray_size_nlogn([1, 1, 1, 1, 1, 1, 1], 11))

