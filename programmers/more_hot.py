def solution(scoville, K):
    from heapq import heappop, heappush
    answer = 0
    #스코빌 가장 작은 값이 앞으로 오게 한번 정렬
    scoville.sort()

    # 섞기
    # scoville 두개 이상 있거나 스코빌의 가장 작은 값이 K보다 작으면 섞기 진행
    while len(scoville)>1 and scoville[0]<K:
        mini1 = heappop(scoville)
        mini2 = heappop(scoville)
        heappush(scoville,(mini1 + (mini2*2)))
        answer+=1
        print(scoville)

    print(answer)
    # 섞기가 끝났다면 마지막 하나 남았거나 모든 스코빌이 K 이상이라는 뜻, 
    # 스코빌에 남은 값 중 제일 작은 값이 K보다 작다면 실패 -1
    if scoville[0]<K:
        return -1

    return answer

solution([1, 2, 3, 9, 10, 12], 7)