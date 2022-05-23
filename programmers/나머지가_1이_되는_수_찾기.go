func solution(n int) int {
    for i:=1;i<n;i++{
        if a:=(n%i); a==1{
            return i
        }
    }
    return 0
}