#!/usr/bin/python3
"""return list of k""" 

def binomial(n, k):
 
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
 
    return binomial(n-1, k-1) + binomial(n-1, k)

def probability(n):
   listprob = []
   list_cnk = []
   if isinstance(n, int) == False:
      return None
   for i in range(0, (n + 1)):
      listprob.append(int(i))
   for a in range (0 , len(listprob)):
   
      
      a = binomial(n, listprob[a])
      list_cnk.append(int(a))
   return list_cnk