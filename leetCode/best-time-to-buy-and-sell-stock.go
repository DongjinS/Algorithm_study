func maxProfit(prices []int) int {
    cur_min := 10001
    answer := 0
    for i:=0;i<len(prices);i++{
        if cur_min>prices[i]{
            cur_min = prices[i]   
        }
        if answer<prices[i]-cur_min{
            answer = prices[i]-cur_min
        }
        
    }
    return answer
}