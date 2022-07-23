#!/usr/bin/python3  
""" recursive program to swap every two adjacent nodes
and return its head. If the number of
nodes is odd, then we need to pairwise swap all
the elements except the last element."""


class Node:
  

    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  

    def pairwiseSwap(self):
        temp = self.head
  
        if temp is None:
            return
  

        while(temp and temp.next):
  

           if(temp.data != temp.next.data):
  
                temp.data, temp.next.data = temp.next.data, temp.data
  
                temp = temp.next.next
  