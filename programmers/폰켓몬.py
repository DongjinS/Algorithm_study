def solution(nums):
    from collections import defaultdict
    answer = 0
    pokemon_dict = defaultdict(int)
    for n in nums:
        pokemon_dict[n]+=1
    
    if len(nums)//2 == len(pokemon_dict.keys()):
        answer = len(nums)//2
    else:
        answer = min(len(pokemon_dict.keys()), len(nums)//2)
    return answer