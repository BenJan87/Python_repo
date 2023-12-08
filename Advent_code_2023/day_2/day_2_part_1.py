import re

def get_game_id(line):
    game_id_match = re.search(r"Game \d+", line)
    return int(game_id_match.group()[5:game_id_match.end() + 1])

def check_if_possible(line: str):
    max_red = 12
    max_green = 13
    max_blue = 14

    red_games = [int(el.replace(" red", "")) for el in re.findall(r"\d+\sred", line)]
    green_games = [int(el.replace(" green", "")) for el in re.findall(r"\d+\sgreen", line)]
    blue_games = [int(el.replace(" blue", "")) for el in re.findall(r"\d+\sblue", line)]

    maximum_value = max(len(red_games), len(green_games), len(blue_games))

    for i in range(maximum_value - len(red_games)):
        red_games.append(0)
    for i in range(maximum_value - len(green_games)):
        green_games.append(0)
    for i in range(maximum_value - len(blue_games)):
        blue_games.append(0)

    error = False
    for green, red, blue in zip(green_games, red_games, blue_games):
        if red > max_red or green > max_green or blue > max_blue:
            error = True
            break
    
    if error:
        return False
    return True
        

if __name__ == "__main__":
    id_list = []
    with open("day_2_input.txt", "r") as file:
        for line in file.readlines():
            if check_if_possible(line):
                id_list.append(get_game_id(line))
    print(sum(id_list))
