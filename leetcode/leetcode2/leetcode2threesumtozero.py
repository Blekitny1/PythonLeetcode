def three_sum_to_zero(nums: list[int]) -> list[list[int]]:
    result = []

    if nums.count(0) == 3:
        result.append([0, 0, 0])

    positive_nums = [_ for _ in nums if _ >= 0]
    negative_nums = [_ for _ in nums if _ < 0]

    positive_sums, negative_sums = {}, {}
    for i, value_i in enumerate(positive_nums):
        for j, value_j in enumerate(positive_nums):
            if i < j:
                positive_sums[(value_i, value_j)] = value_i + value_j

    for i, value_i in enumerate(negative_nums):
        for j, value_j in enumerate(negative_nums):
            if i < j:
                negative_sums[(value_i, value_j)] = value_i + value_j

    for key, value in positive_sums.items():
        for num in negative_nums:
            if value + num == 0:
                result.append(list(key) + [num])

    for key, value in negative_sums.items():
        for num in positive_nums:
            if value + num == 0:
                result.append(list(key) + [num])



    return result

def three_sum_to_zero_yt(nums: list[int]):
    result = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and nums[index - 1] == value:
            continue

        left, right = index + 1, len(nums) - 1
        while left < right:
            current_sum = value + nums[left] + nums[right]
            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                result.append([value, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result


if __name__ == '__main__':
    print(three_sum_to_zero([-1, 0, 1, 2, -1, -4]))
    print(three_sum_to_zero([0, 1, 1]))
    print(three_sum_to_zero([0, 0, 0]))
    print(three_sum_to_zero_yt([-1, 0, 1, 2, -1, -4]))
    print(three_sum_to_zero_yt([0, 1, 1]))
    print(three_sum_to_zero_yt([0, 0, 0]))

