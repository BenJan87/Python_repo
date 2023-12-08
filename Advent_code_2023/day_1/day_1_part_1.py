
def finding_digits(word: str) -> str:

    for char in word:
        if char.isdigit():
            fst_digit = char
            break

    for char in word[::-1]:
        if char.isdigit():
            last_digit = char
            break

    return int(fst_digit + last_digit)


if __name__ == "__main__":
    digits = []
    with open('day_1_input.txt', 'r') as file:
        for line in file.readlines():
            digits.append(finding_digits(line))
    print(sum(digits))
