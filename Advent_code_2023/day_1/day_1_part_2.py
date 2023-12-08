from day_1_part_1 import finding_digits
import re


def find_all(word: str) -> int:
    number_dict = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
    }

    starting_list = []
    for number_as_word in list(number_dict.keys()):
        starting_list.append((number_dict[number_as_word], re.search(number_as_word, word)))
    
    
    without_none_sorted_list = [(el[0], el[1].span()[0]) for el in starting_list if el[1] is not None]
    sorted_starting_list = sorted(without_none_sorted_list, key=lambda x: x[1])

    # [(liczba, miejsce wystąpienia)]
    
    fst_digit = sorted_starting_list[0][0] if sorted_starting_list else 0
    last_digit = sorted_starting_list[-1][0] if sorted_starting_list else 0 

    for i in range(len(word)):
        if word[i].isdigit() and sorted_starting_list:
            if sorted_starting_list[0][1] > i:
                fst_digit = word[i]
                break

    for i in range(len(word) - 1, -1, -1):
        if word[i].isdigit() and sorted_starting_list:
            if sorted_starting_list[-1][1] < i:
                last_digit = word[i]
                break
            
    return int(fst_digit + last_digit)
    



if __name__ == "__main__":
    # digits = []
    
    # with open(r'C:\Users\Benek\Desktop\Studia_AGH\git_repos\Python_repo\Advent_code_2023\day_1\day_1_input.txt', 'r') as file:
    #     for line in file.readlines():
    #         digits.append(find_all(line))

    # print(sum(digits))   

    print(find_all('1tcrgthmeight5mssseight'))