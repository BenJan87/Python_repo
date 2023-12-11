import re

def point_from_line(line):
    split_char_position = re.search(r"\|", line)
    win_numbers_string = line[:split_char_position.start()]
    our_numbers_string = line[split_char_position.start() + 1:]

    win_numbers_list = re.findall(r"\d+", win_numbers_string)
    our_numbers_list = re.findall(r"\d+", our_numbers_string)

    count = 0
    for number in our_numbers_list:
        if number in win_numbers_list:
            count += 1

    return 2**(count - 1) if count > 0 else 0


if __name__ == "__main__":
    sum = 0
    with open(r"day_4_input.txt", "r") as file:
        for line in file.readlines():
            pattern = r"Card\s+\d+:"
            stripped_line = re.sub(pattern, "", line)
            sum += point_from_line(stripped_line)
    print(sum)