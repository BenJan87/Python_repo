import re

def open_file_and_fill_inside_matrix(file_path):
    with open(file_path, "r") as file:
        matrix = [el.rstrip() for el in file.readlines()]
    return matrix


def check_adjacent(start_pos, end_pos, matrix):
    for i in range(start_pos, end_pos + 1):
        one = 
        two = 
        three =
        four = 
        five = 
        six = 
        seven = 
        eight =
# input_line = "....0234...123"
# pattern = r'\d+'

# matches = re.finditer(pattern, input_line)

# for match in matches:
#     matched_string = match.group()
#     start_index = match.start()
#     end_index = match.end() - 1  # Adjust end_index to get the correct position

if __name__ == "__main__":
    matrix = open_file_and_fill_inside_matrix(r)