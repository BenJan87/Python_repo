#find max pairs with minimun differences
def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    count = 0
    i = 0
    while i != len(skillLevel):
        flag = 0
        for j in range(i + 1, len(skillLevel)):
            if skillLevel[i] + minDiff <= skillLevel[j]:
                el_1, el_2 = skillLevel[i], skillLevel[j]
                skillLevel.remove(el_1)
                skillLevel.remove(el_2)
                count += 1
                flag += 1
                break
        if len(skillLevel) == 0:
            break
        if flag != 1:
            i += 1
        else:
            i = 0
        
    return count

if __name__ == "__main__":
    print(maxPairs([1,2,3,4,5,6], 4))