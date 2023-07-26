class Solution{
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
        ListNode newNode = new ListNode(0); //create an empty linkedlist;
        //compare the data, smaller ones get into empty linkedlist:
        while (l1!= null && l2 != null){
            if(l1.val < l2.val){
                newNode.next = l1;
                l1 = l1.next;
            }
            else {
                newNode.next = l2;
                l2 = l2.next;
            }
            newNode = newNode.next;
        }
        //* after while loop, if l2 is null, rest of the l1 all goes to newNode */
        if (l1!= null){
            newNode.next = l1;
        }
        //* else, rest of the l2 goes to newNode */
        else{
            newNode.next = l2;
        }
        return newNode.next;
        }   
}