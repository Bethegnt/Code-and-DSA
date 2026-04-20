# Last updated: 20/04/2026, 23:21:38
# Linkedlist+circular conversion + two pointer
1
2# Definition for singly-linked list.
3# class ListNode:
4#     def __init__(self, x):
5#         self.val = x
6#         self.next = None
7
8class Solution:
9    def rotateRight(self, head: ListNode, k: int) -> ListNode:
10        
11        if not head:
12            return None
13        
14        lastElement = head
15        length = 1
16        while ( lastElement.next ):
17            lastElement = lastElement.next
18            length += 1
19        k = k % length
20        lastElement.next = head
21        tempNode = head
22        for _ in range( length - k - 1 ):
23            tempNode = tempNode.next
24        answer = tempNode.next
25        tempNode.next = None
26        
27        return answer
28