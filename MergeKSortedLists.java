/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }
        if(lists.length == 1){
            return lists[0];
        }
        ListNode val = merge2Lists(lists[0], lists[1]);
        for(int i = 2; i < lists.length; i++){
            val = merge2Lists(val, lists[i]);
        }
        return val;
    }

    public ListNode merge2Lists(ListNode list1,ListNode list2){
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        if(list1.val < list2.val){
            list1.next = merge2Lists(list1.next, list2);
            return list1;
        }
        else{
            list2.next = merge2Lists(list1, list2.next);
            return list2;
        }
    }
}