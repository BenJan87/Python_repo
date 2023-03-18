def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_no_dup = sorted(list(set(ranked)), reverse=True)
    positions = []


    for score in player:
        while ranked_no_dup and score >= ranked_no_dup[-1]:
            ranked_no_dup.pop()
            
        positions.append(len(ranked_no_dup) + 1)
    
    return positions

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    for el in result:
        print(el)
