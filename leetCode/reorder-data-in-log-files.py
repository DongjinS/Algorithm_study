class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        from collections import defaultdict
        let_log_dict = defaultdict(list)
        digit_log = []
        answer = []
        for log in logs:
            log = log.split(" ")
            if log[1].isalpha():
                let_log_dict[" ".join(log[1:])].append(log[0])
            else:
                digit_log.append(" ".join(log))
        
        for key in sorted(list(let_log_dict.keys())):
            for identifier in sorted(let_log_dict[key]):
                answer.append(identifier+" "+key)
        
        answer+=digit_log
        return answer

print(Solution.reorderLogFiles(Solution, ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(Solution.reorderLogFiles(Solution, ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))