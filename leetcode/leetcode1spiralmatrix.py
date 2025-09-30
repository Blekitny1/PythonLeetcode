from unittest import result


def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    result = []
    def pop_top_row_and_append_elements_to_result(matrix: list[list[int]], result: list[int]):
        result.extend(matrix[0])
        return matrix[1:], result

    def pop_bottom_row_and_append_elements_to_result(matrix: list[list[int]], result: list[int]):
        result.extend(matrix[-1][::-1])
        return matrix[:-1], result

    def pop_left_column_and_append_elements_to_result(matrix: list[list[int]], result: list[int]):
        for row_num in range(len(matrix) - 1, 0, -1):
            result.append(matrix[row_num][0])
            matrix[row_num] = matrix[row_num][1:]
        return matrix, result

    def pop_right_column_and_append_elements_to_result(matrix: list[list[int]], result: list[int]):
        for row_num in range(len(matrix)):
            result.append(matrix[row_num][-1])
            matrix[row_num] = matrix[row_num][:-1]
        return matrix, result

    while len(matrix) > 0:
        matrix, result = pop_top_row_and_append_elements_to_result(matrix, result)
        if len(matrix) == 0:
            break
        matrix, result = pop_right_column_and_append_elements_to_result(matrix, result)
        if len(matrix) == 0:
            break
        matrix, result = pop_bottom_row_and_append_elements_to_result(matrix, result)
        if len(matrix) == 0:
            break
        matrix, result = pop_left_column_and_append_elements_to_result(matrix, result)

    return result


def spiral_matrix_yt(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix: #works as len(matrix) > 0 as list.toBoolean = list.notEmpty

        #1 add first row to result
        result += matrix.pop(0)

        #2 append last element of each row in order
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        #3 append reversed last row
        if matrix:
            result += matrix.pop()[::-1]

        #4 append first element of matrix reversed by rows
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result



if __name__ == '__main__':
    print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
    print(spiral_matrix_yt([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_matrix_yt([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
