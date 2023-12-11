def open_file_and_fill_inside_matrix(file_path):
    with open(file_path, "r") as file:
        matrix = [el.rstrip() for el in file.readlines()]
    return matrix

def check_adjacent(line, column, matrix):
    one = [-1, -1]
    two = [0, -1]
    three = [1, -1]
    four = [-1, 0]
    five = [1, 0]
    six = [-1, 1]
    seven = [0, 1]
    eight = [1, 1]

    new_pos = [line + one[0], column + one[1]]
    if matrix[new_pos[0], new_pos[1]].isdigit():
        for i in range(new_pos[1], 0, -1):
            


if __name__ == "__main__":
    test_file = r'day_3_input.txt'
    sum = 0
    matrix = open_file_and_fill_inside_matrix(test_file)
    for index_of_line, line in enumerate(matrix):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            matched_string = match.group()
            start_index = match.start()
            end_index = match.end() - 1  
            if check_adjacent(start_index, end_index, index_of_line, matrix):
                sum += int(matrix[index_of_line][start_index:end_index + 1])
    print(sum)