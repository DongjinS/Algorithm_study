def solution(begin, target, words):
    from collections import deque
    answer = 0 
    begin = list(begin)
    target = list(target)
    words = list(map(lambda x: list(x) , words))
    candidate = []
    if target not in words:
        return 0
    
    for word in words:
        visited = set()
        diff = 0
        cnt = 0
        for i in range(len(word)):
            if word[i] != begin[i]:
                diff+=1
        if diff == 1:
            visited.add("".join(word))
            cnt += 1
            dfs(word,words,visited,cnt,candidate,target)
    
    answer = min(candidate)
    return answer

def dfs(word,words,visited,cnt,candidate,target):
    if word == target:
        candidate.append(cnt)
        return
    for new_word in words:
        if "".join(new_word) in visited:continue
        diff = 0
        for i in range(len(new_word)):
            if new_word[i] != word[i]:
                diff+=1
        if diff == 1:
            visited.add("".join(new_word))
            cnt+=1
            dfs(new_word,words,visited,cnt,candidate,target)
            cnt-=1
            visited.remove("".join(new_word))
    return

# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.3MB)
# 테스트 3 〉	통과 (0.49ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)