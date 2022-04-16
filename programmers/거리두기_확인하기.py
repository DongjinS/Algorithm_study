def chk(location, place):
    for i in range(len(location)-1):
        for j in range(i+1, len(location)):
            if abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1]) <= 2:
                if abs(location[i][0] - location[j][0]) == 0:
                    if place[location[i][0]][location[i][1]+1] == "X":
                        continue
                elif abs(location[i][1] - location[j][1]) == 0:
                    if place[location[i][0]+1][location[i][1]] == "X":
                        continue
                else:
                    if place[location[i][0]][location[j][1]] == "X" and place[location[j][0]][location[i][1]] == "X":
                        continue
                return False
    return True

def solution(places):
    answer = []
    for place in places:
        place = list(map(list, place))
        location = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    location.append([i,j])
        if not chk(location, place):
            answer.append(0)
        else:
            answer.append(1)
            
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])