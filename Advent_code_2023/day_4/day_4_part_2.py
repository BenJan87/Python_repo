import re

def find_scratches(line, xdf):






if __name__ == "__main__":
    sum = 0
    with open(r"day_4_input.txt", "r") as file:
        for line in file.readlines():
            pattern = r"Card\s+\d+:"
            stripped_line = re.sub(pattern, "", line)
            sum += point_from_line(stripped_line)
    print(sum)