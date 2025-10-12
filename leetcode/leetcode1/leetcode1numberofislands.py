def number_of_islands(areas: list[list[str]]) -> int:

    def area_is_land_and_has_adjacent_land(areas, x_coord: int, y_coord: int) -> bool:
        return area_is_land_and_has_land_up(areas, x_coord, y_coord) \
            or area_is_land_and_has_land_down(areas, x_coord, y_coord) \
            or area_is_land_and_has_land_left(areas, x_coord, y_coord) \
            or area_is_land_and_has_land_right(areas, x_coord, y_coord)

    def area_is_land_and_has_land_up(areas, x_coord: int, y_coord: int) -> bool:
        if x_coord == 0:
            return False
        elif areas[x_coord][y_coord] == "1" and int(areas[x_coord - 1][y_coord]) > 1:
            areas[x_coord][y_coord] = areas[x_coord - 1][y_coord]
            return True
        else:
            return False

    def area_is_land_and_has_land_down(areas, x_coord: int, y_coord: int) -> bool:
        if x_coord == len(areas) - 1:
            return False
        elif areas[x_coord][y_coord] == "1" and int(areas[x_coord + 1][y_coord]) > 1:
            return True
        else:
            return False

    def area_is_land_and_has_land_left(areas, x_coord: int, y_coord: int) -> bool:
        if y_coord == 0:
            return False
        if areas[x_coord][y_coord] == "1" and int(areas[x_coord][y_coord - 1]) > 1:
            areas[x_coord][y_coord] = areas[x_coord][y_coord - 1]
            return True
        else:
            return False

    def area_is_land_and_has_land_right(areas, x_coord: int, y_coord: int) -> bool:
        if y_coord == len(areas[0]) - 1:
            return False
        elif areas[x_coord][y_coord] == "1" and int(areas[x_coord][y_coord + 1]) > 1:
            return True
        else:
            return False

    # jesli 1 i nie ma obok > 1 to zrób nastepna wyspe e.g. 2
    # jesli 1 i obok jest > 1 to zastąp 1 tym nrem
    # jesli 0 to nic nie rob
    # zwroc nrek ktorym nazywalismy wyspy - 1, bo nrjemy od 2

    counter = 1
    for i in range(len(areas)):
        for j in range(len(areas[0])):
            if areas[i][j] == "1" and not area_is_land_and_has_adjacent_land(areas, i, j):
                counter += 1
                areas[i][j] = str(counter)


    return counter - 1

def number_of_islands_yt(areas: list[list[int]]):
    #implemented bfs algorithm, accumulating set of visited points instead of marking them with assigning number to island like I did
    return 7


if __name__ == '__main__':
    print(number_of_islands([["1", "1", "1"], ["1", "1", "0"], ["1", "0", "0"]]))
    print(number_of_islands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
    #print(number_of_islands_yt([[1, 1], [3, 4], [-1, 0]]))
    #print(number_of_islands_yt([[3, 2], [-2, 2]]))

