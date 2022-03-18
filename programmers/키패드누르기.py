def solution(numbers, hand):
    from collections import defaultdict
    answer = ''
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    
    tmp = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    
    dict = defaultdict(list)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            dict[tmp[i][j]] = [i,j]
    
    left_preferred = [1,4,7]
    right_preferred = [3,6,9]
    last_lhand = 10
    last_rhand = 12
    
    for n in numbers:
        if n in left_preferred:
            answer+="L"
            last_lhand = n
        elif n in right_preferred:
            answer+="R"
            last_rhand = n
        else:
            if abs((dict[last_lhand][0] - dict[n][0])) + abs(dict[last_lhand][1]-dict[n][1]) > abs((dict[last_rhand][0]-dict[n][0])) + abs(dict[last_rhand][1]-dict[n][1]):
                answer+="R"
                print(n, last_lhand, last_rhand)
                last_rhand = n
            elif abs((dict[last_lhand][0] - dict[n][0])) + abs(dict[last_lhand][1]-dict[n][1]) < abs((dict[last_rhand][0]-dict[n][0])) + abs(dict[last_rhand][1]-dict[n][1]):
                answer+="L"
                last_lhand = n
            else:
                if hand == "right":
                    answer+="R"
                    last_rhand = n
                else:
                    answer+="L"
                    last_lhand = n 

    return answer