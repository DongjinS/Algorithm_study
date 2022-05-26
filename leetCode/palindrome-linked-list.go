/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func isPalindrome(head *ListNode) bool {
    
    var arr [] int
    
    for cur:=head;cur!=nil;cur=cur.Next{
        arr = append(arr,cur.Val)
    }
    
    fmt.Println(arr)
    var n = len(arr)
    var half_n = int(n/2)
    
    for i:=0; i<half_n;i++{
        if arr[i]!=arr[n-1-i]{
            return false
        }
    }
    
    return true
}