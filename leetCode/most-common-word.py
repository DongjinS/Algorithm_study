class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        word_dict = defaultdict(int)
        
        answer = ("",0)
        banned = set(banned)
        words = [word for word in re.sub(r'[^\w ]',' ',paragraph).lower().split() if word not in banned]
        
        for word in words:
            word_dict[word]+=1
            if answer[1]<word_dict[word]:
                answer = (word,word_dict[word])
        return answer[0]