from operator import indexOf


def two_sum(nums: list[int], target: int):
    complements_to_target = [target - _ for _ in nums]
    for i, num in enumerate(nums):
        if num in complements_to_target and i != complements_to_target.index(num):
           return [i, indexOf(nums, target - num)]
    return None


def two_sum_2(nums: list[int], target: int):
    target_dict = {} #num, index
    for i, num in enumerate(nums):
        numm_complement = target - num
        if numm_complement in target_dict:
            return [i, target_dict[numm_complement]]
        else:
            target_dict[num] = i
    return None


if __name__ == '__main__':
    print(two_sum([1, 1], 2))
    print(two_sum([6, 2, 3, 4, 4, 2, 1, 8], 14))
    print(two_sum([3, 4, 2], 6))
    print(two_sum_2([1, 1], 2))
    print(two_sum_2([6, 2, 3, 4, 4, 2, 1, 8], 14))
    print(two_sum_2([3, 4, 2], 6))

