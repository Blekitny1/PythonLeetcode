def min_visiting_time(points: list[list[int]]) -> int:
    list_of_following_pairs = [[points[i], points[i + 1]] for i in range(len(points) - 1)]
    total_visiting_time: int = 0
    for pair in list_of_following_pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        total_visiting_time += max(x_diff, y_diff)

    return total_visiting_time

def min_visiting_time_yt(points: list[list[int]]):
    res = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        res += max(abs(x1 - x2), abs(y1 - y2))
        x1, y1 = x2, y2
    return res


if __name__ == '__main__':
    print(min_visiting_time([[1, 1], [3, 4], [-1, 0]]))
    print(min_visiting_time([[3, 2], [-2, 2]]))
    print(min_visiting_time_yt([[1, 1], [3, 4], [-1, 0]]))
    print(min_visiting_time_yt([[3, 2], [-2, 2]]))

