import re

def find_all(word: str) -> int:
    number_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }

    fst_char_from_word, last_char_from_word = None, None
    fst_char_from_digit, last_char_from_digit = None, None

    fst_char_from_word_index, last_char_from_word_index = len(word), -1
    fst_char_from_digit_index, last_char_from_digit_index = len(word), -1

    flag_1 = 0
    flag_2 = 0

    for i in range(len(word)):
        five_char_word = word[i:i + 5]
        for number_as_word in number_dict:
            match = re.search(number_as_word, five_char_word)
            if match:
                fst_char_from_word = number_dict[number_as_word]
                fst_char_from_word_index = match.start() + i
                flag_1 = 1
                break
        if flag_1:
            break

    for i in range(len(word)):
        five_char_word = word[len(word) - i - 5:len(word) - i]
        for number_as_word in number_dict:
            match = re.search(number_as_word, five_char_word)
            if match:
                last_char_from_word = number_dict[number_as_word]
                last_char_from_word_index = len(word) - i - 5 + match.start()
                flag_2 = 1
                break
        if flag_2:
            break

    for i, char in enumerate(word):
        if char.isdigit():
            fst_char_from_digit = char
            fst_char_from_digit_index = i
            break

    for i, char in enumerate(word[::-1]):
        if char.isdigit():
            last_char_from_digit = char
            last_char_from_digit_index = len(word) - i - 1
            break


    if fst_char_from_digit_index < fst_char_from_word_index:
        fst = fst_char_from_digit
    else:
        fst = fst_char_from_word

    if last_char_from_digit_index > last_char_from_word_index:
        last = last_char_from_digit
    else:
        last = last_char_from_word

    return int(fst + last)


if __name__ == "__main__":
    digits = []
    with open('day_1_input.txt', 'r') as file:
        for line in file.readlines():
            digits.append(find_all(line))
    print(sum(digits))