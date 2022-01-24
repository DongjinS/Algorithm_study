# https://velog.io/@tjdud0123/%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
def solution(n, weak, dist):
    answer = 0
    repair_list = [()] # 점검 가능 영역 리스트 , 첫 공집합 초기화
    count = 0 # 점검에 사용된 친구 명수 체크
    W, F = len(weak), len(dist) #취약 지점 개수 W, 친구 명수 F
    dist.sort(reverse = True)

    for cur_f in dist: #가장 이동거리 먼 친구부터 점검 가능 영역 체크
        cur_repairs = []
        count += 1

        for i, weak_p in enumerate(weak): #현재 친구가 수리가능한 영역 체크, 모든 취약 지점은 시작점으로 순회 체크
            start = weak_p
            ends = weak[i:] + [n+w for w in weak[:i]] # 현재 시작점 i 으로 i 전까지의 취약 지점 [1,5,6,10]에서 i 6 -> [6,10,13,17] 
            can  = [end%n for end in ends if end-start<=cur_f] # 취약 지점중에 start로 부터 현재 친구의 이동거리보다 적게 떨어진 위치만 can list에 추가, 취약지점 개수로 나누어서 원래 위치 번호로 바꿔준다
            cur_repairs.append(can) #현재 친구가 각 start에서 시작해서 점검할 수 있는 취약지점의 조합 repairs에 추가

        #현재 친구가 점검할 수 있는 조합과 이전 친구들이 수리할 수 있는 조합을 합쳐서 현재까지 투입된 친구들이 수리할 수 있는 영역 체크
        new_repair_list = set()
        for cur_r in cur_repairs:
            for last_repair in repair_list:
                new_repair = set(cur_r) | set(last_repair) # 현재 친구 점검 가능 영역과 이전 점검 가능 영역 합침
                if len(new_repair) == W:
                    return count
                new_repair_list.add(tuple(new_repair))
        
        repair_list = list(new_repair_list)

    return -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]), 2)
print(solution(12, [1, 3, 4, 9, 10],[3, 5, 7]),	1)


#그리디 하게 해볼려다 버림..
from collections import deque
def solution2(n, weak, dist):
    weak2 = [weak[-1] - n]
    weak2.extend(weak[:-1]) # [-2, 1, 5, 6]
    print(weak2)

    #연결거리 짧은거 찾기
    tmp1 = 0
    tmp2 = 0
    for i in range(len(weak)-1):
        tmp1 += weak[i+1]-weak[i]
        tmp2 += weak2[i+1]-weak2[i]
    
    print(tmp1, tmp2)
    if tmp1<=tmp2:
        weak_dist = tmp1
    else:
        weak_dist = tmp2
        weak = weak2

    #이동거리 긴 친구부터 취약지점의 사이가 가장 긴 취약지점부터 점검하도록 하고 점검한 요소 제거후 취약지점 거리 다시 측정
    dist.sort()

    tmp = []
    for i in range(len(weak)-1):
            tmp.append(weak[i+1] - weak[i])
    weak = deque(tmp)
    
    cnt = 0
    while dist and weak:
        print(weak)
        f_dist = dist.pop()
        print(f_dist, weak_dist)
        if f_dist>=weak_dist:
            weak = []
            cnt+=1
            continue
        
        while weak and weak[0]<=f_dist:
            f_dist -= weak.popleft()
        
        if len(weak) > 1:
            weak.popleft()

        weak_dist = sum(weak)
        cnt += 1

    answer = cnt
    return answer
