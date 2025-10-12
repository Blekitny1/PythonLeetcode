import math

def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    list_of_sliced_lists = [nums[i:i + k + 1] for i in range(len(nums) - k)]
    return bool(sum([len(set(_)) < len(_) for _ in list_of_sliced_lists]))

def contains_nearby_duplicate_yt(nums: list[int], k: int):
    seen = set()
    for index, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[index - k])
    return False


if __name__ == '__main__':
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))
    print(contains_nearby_duplicate([1, 0, 1, 1], 1))
    print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
    print(contains_nearby_duplicate_yt([1, 2, 3, 1], 3))
    print(contains_nearby_duplicate_yt([1, 0, 1, 1], 3 ))
    print(contains_nearby_duplicate_yt([1, 2, 3, 1, 2, 3], 2))

