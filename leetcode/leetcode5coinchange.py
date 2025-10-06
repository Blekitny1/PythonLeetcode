def coin_change(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    acc_result_dict = {}
    current_iteration_result_dict = {}
    for coin in coins:
        acc_result_dict[amount - coin] = 1
    while True:
        acc_result_dict.update(current_iteration_result_dict)
        if 0 in acc_result_dict.keys():
            return acc_result_dict[0]
        if min(acc_result_dict.keys()) < -max(coins):
            return -1
        current_iteration_result_dict = {}
        for key, value in acc_result_dict.items():
            for coin in coins:
                if key - coin not in acc_result_dict.keys():
                    current_iteration_result_dict[key - coin] = acc_result_dict[key] + 1


    return 0

def coin_change_yt(coins: list[int], amount: int) -> int:
    array_of_min_coin_distributions = [amount + 1] * (amount + 1) #as we need arr[amount]
    array_of_min_coin_distributions[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                array_of_min_coin_distributions[i] = min(array_of_min_coin_distributions[i], array_of_min_coin_distributions[i - coin] + 1)
    return array_of_min_coin_distributions[amount] if (array_of_min_coin_distributions[amount] != amount + 1) else -1


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
    print(coin_change([5, 40, 50], 85))
    print(coin_change([2, 40], 85))
    print(coin_change_yt([1, 2, 5], 11))
    print(coin_change_yt([5, 40, 50], 85))
    print(coin_change_yt([2, 40], 85))

