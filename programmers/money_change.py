def solution2(n, money):
    answer = 0
    target = n
    N = len(money)
    dp = [0 for x in range(N)]
    # print(dp)

    # 주어진 화폐마다 5원을 만들 수 있는 경우의수
    for i in range(N):
        if i>0:
            dp[i] = dp[i-1]%1000000007
        if target//money[i]>=1:
            if target%money[i] == 0:
                dp[i]+=1%1000000007
            for j in range(i):
                if money[i] + money[j] > target:
                    break
                n = 1
                while target - money[i] * n > 0:
                    if (target - money[i] * n)%money[j] == 0:
                        dp[i]+=1%1000000007
                        n+=1
                    else:break
        else:
            break

    return max(dp)%1000000007

def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n+1)]
    # print(dp)

    # 1원부터주어진 돈까지 경우의 수 dp 테이블 채우기
    for coin in money:
        dp[coin] += 1
        for j in range(coin,n+1): 
            dp[j] += dp[j-coin]
        print(dp)
    
    return dp[-1]

print(solution(5,[1,2,5]),4)
print(solution(5,[1,2,3,5]),6)