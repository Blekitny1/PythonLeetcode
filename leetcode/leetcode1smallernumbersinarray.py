from operator import indexOf


def count_smaller_nums(nums: list[int]) -> list[int]:
    n = len(nums)
    result = []
    for i in range(n):
        counter = 0
        for j in range(n):
            if i!= j and nums[i] > nums[j]:
                counter += 1
        result.append(counter)
    return result

def count_smaller_nums_yt(nums: list[int]) -> list[int]:
    return [indexOf(sorted(nums), num) for num in nums]

if __name__ == '__main__':
    print(count_smaller_nums([8, 1, 2, 2, 3]))
    print(count_smaller_nums([6, 5, 4, 8]))
    print(count_smaller_nums([3, 3, 3]))
    print(count_smaller_nums_yt([8, 1, 2, 2, 3]))
    print(count_smaller_nums_yt([6, 5, 4, 8]))
    print(count_smaller_nums_yt([3, 3, 3]))

