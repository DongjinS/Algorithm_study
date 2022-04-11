def solution(n, k):
    answer = 0
    cur = n
    k_num = []
    while cur != 0:
        k_num.append(str(cur % k))
        cur = cur//k
    
    k_num.reverse()
    k_num = "".join(k_num).split("0")
    
    print(k_num)
    for num in k_num:
        if num == '':
            continue
        else:
            cur = int(num)
        flag = True
        for d in range(2,int(cur**.5)+1):
            # print(cur, int(cur**.5))
            if cur%d == 0:
                flag = False
                break
        if cur!= 1 and flag:
            answer += 1
    return answer