func productExceptSelf(nums []int) []int {
    var answer [] int
    tmp := 1
    for i:=0;i<len(nums);i++{
        answer = append(answer,tmp)
        tmp=tmp*nums[i]
    }
    tmp=1
    for i:=len(nums)-1;i>=0;i--{
        answer[i]=tmp*answer[i]
        tmp=nums[i]*tmp
    }
    
    return answer
}