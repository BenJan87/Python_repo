def climbingLeaderboard(ranked, player) -> int:
    positions = []
    ranked = sorted(list(set(ranked)), reverse=True)
    
    dict_ranked = {f"{i + 1}": ranked[i] for i in range(len(ranked))}
    flag = False
    for result in player:

        for key, val in dict_ranked.items():
            if result >= val:
                positions.append(int(key))
                flag = True
                break

        if not flag:
            positions.append(len(dict_ranked) + 1) 

    return positions


if __name__ == '__main__':

    ranked = list(map(int, input().rstrip().split()))

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
