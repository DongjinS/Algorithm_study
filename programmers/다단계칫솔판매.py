def solution(enroll, referral, seller, amount):
    from collections import defaultdict
    answer = []
    tree_dict = defaultdict(str)
    money_dict = defaultdict(int)
    N = len(enroll)
    for i in range(N):
        tree_dict[enroll[i]] = referral[i]
        money_dict[enroll[i]] = 0
    # print(tree_dict)
    sell_amount = list(zip(seller, amount))
    
    for name, amount in sell_amount:
        cur_name = name
        cur_amount = amount*100
        while tree_dict[cur_name] != "" and cur_amount>0:
            # print(cur_name)
            next_name = tree_dict[cur_name]
            next_amount = cur_amount//10
            if next_amount>0:
                money_dict[cur_name] += cur_amount - next_amount
            else:
                money_dict[cur_name] += cur_amount
            
            cur_name = next_name
            cur_amount = next_amount
            
    answer = list(money_dict.values())
    return answer