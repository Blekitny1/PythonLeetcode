import collections

def sorted_squares(nums: list[int]) -> list[int]:
    result = []
    negative_nums, positive_nums = [_ for _ in nums if _ < 0], [_ for _ in nums if _ >= 0]
    positive_nums = [_ ** 2 for _ in positive_nums]
    negative_nums = [_ ** 2 for _ in reversed(negative_nums)]
    while len(positive_nums) > 0 or len(negative_nums) > 0:
        if not positive_nums:
            result.append(negative_nums.pop(0))
        elif not negative_nums:
            result.append(positive_nums.pop(0))
        elif positive_nums[0] < negative_nums[0]:
            result.append(positive_nums.pop(0))
        else:
            result.append(negative_nums.pop(0))

    return result

def sorted_squares_yt(nums: list[int]):
    result = collections.deque()
    left_index, right_index = 0, len(nums) - 1
    while left_index <= right_index:
        left_value, right_value = abs(nums[left_index]), abs(nums[right_index])
        if left_value > right_value:
            result.appendleft(left_value * left_value)
            left_index += 1
        else:
            result.appendleft(right_value * right_value)
            right_index -= 1
    return list(result)


if __name__ == '__main__':
    print(sorted_squares([-4, -1, 0, 3, 10]))
    print(sorted_squares([-7, -3, 2, 3, 11]))
    print(sorted_squares_yt([-4, -1, 0, 3, 10]))
    print(sorted_squares_yt([-7, -3, 2, 3, 11]))

