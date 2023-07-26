class Solution{
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
        ListNode newNode = new ListNode(0);
        while (l1!= null && l2 != null){
            if(l1.val < l2.val){
                newNode.next = l1;
                l1 = l1.next;
            }
            else {
                newNode.next = l2;
                l2 = l2.next;
            }
        }
        if (l1!= null){
            current.next = l1;
        }
        else{
            current.next = l2;
        }
        return newNode.next;
        }   
}