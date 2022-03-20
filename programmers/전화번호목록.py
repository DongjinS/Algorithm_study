def solution(phone_book):
    answer = True
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = 1
        
    for phone_number in phone_book:
        tmp = ""
        for n in phone_number:
            tmp += n
            if phone_number != tmp and tmp in dict:
                return False
            
    return answer

solution(["123","456","789"])