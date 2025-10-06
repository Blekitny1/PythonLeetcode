def single_number(nums: list[int]) -> int:
    set_of_elements = set()
    for num in nums:
        if num not in set_of_elements:
            set_of_elements.add(num)
        else:
            set_of_elements.remove(num)

    return set_of_elements.pop()

def single_number_yt(nums: list[int]):
    result = 0
    for num in nums:
        result ^= num #this will cancel with following duplicate, as a^a==0 and a^b^c==a^c^b
    return result


if __name__ == '__main__':
    print(single_number([2]))
    print(single_number([2, 2, 1, 1, 13]))
    print(single_number_yt([2]))
    print(single_number_yt([2, 2, 1, 1, 13]))

