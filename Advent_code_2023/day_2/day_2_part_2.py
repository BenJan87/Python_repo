import re


def power_of_mimimums(line: str):
    max_red = 12
    max_green = 13
    max_blue = 14

    red_games = [int(el.replace(" red", "")) for el in re.findall(r"\d+\sred", line)]
    green_games = [int(el.replace(" green", "")) for el in re.findall(r"\d+\sgreen", line)]
    blue_games = [int(el.replace(" blue", "")) for el in re.findall(r"\d+\sblue", line)]

    max_red = max(red_games) if red_games else 0
    max_green = max(green_games) if green_games else 0
    max_blue = max(blue_games) if blue_games else 0

    return max_red*max_green*max_blue
        

if __name__ == "__main__":
    power_list = []
    with open("day_2_input.txt", "r") as file:
        for line in file.readlines():
            power_list.append(power_of_mimimums(line))
    print(sum(power_list))