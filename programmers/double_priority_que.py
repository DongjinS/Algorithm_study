####I 숫자	큐에 주어진 숫자를 삽입합니다.
####D 1	큐에서 최댓값을 삭제합니다.
####D -1	큐에서 최솟값을 삭제합니다

#1번만 통과 안됨 - 중복 제거 문제
def solution(operations):
    print(operations)
    maxi = 0
    mini = float("INF")
    q = set()

    for oper in operations:
        print(oper, q, mini, maxi)
        oper = oper.split()
        if oper[0] == "I":
            maxi = max(maxi,int(oper[1]))
            mini = min(mini,int(oper[1]))
            q.add(int(oper[1]))
        else:#D
            if mini in q and int(oper[1])==-1:#D-1 최소값 삭제
                q.remove(mini)
                try:
                    mini = min(q)
                except:
                    maxi = 0
                    mini = float("INF")
            elif maxi in q and int(oper[1])==1:#D 1 최대값 삭제
                q.remove(maxi)
                try:
                    maxi = max(q)
                except:
                    maxi = 0
                    mini = float("INF")
    
    print(q)
    
    if q:
        print([max(q), min(q)])
        return [max(q), min(q)]
    else:
        return [0,0]

# solution(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"])


#통과
def solution2(operations):
    from heapq import heappop, heappush
    hq = []
    
    answer = []

    for oper in operations:
        oper = oper.split()
        if oper[0] == "I":
            heappush(hq,int(oper[1]))
            
        else:#D
            if hq and int(oper[1])<0:#D-1 최소값 삭제
                heappop(hq)
            elif hq:#D 1 최대값 삭제
                hq.remove(max(hq))
    

    if len(hq)<2:
        return [0,0]
    print([max(hq),min(hq)])
    return [max(hq),min(hq)]

# solution2(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"])

def solution3(operations):
    from heapq import heappop, heappush
    maxhq = []
    minhq = []
    answer = []

    for oper in operations:
        oper = oper.split()
        if oper[0] == "I":
            heappush(minhq,int(oper[1]))
            heappush(maxhq,-int(oper[1]))
        else:#D
            if int(oper[1])<0:#D-1 최소값 삭제
                heappop(minhq)
                print("D-1", minhq)
            else:#D 1 최대값 삭제
                heappop(maxhq)
                print("D 1", maxhq)
    
    print(minhq, maxhq)
    
    
    for maxi in maxhq:
        if -(maxi) in minhq:
            answer.append(-maxi)
    print(answer)
    if len(answer)<2:
        return [0,0]
    return [max(answer),min(answer)]

solution3(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"])