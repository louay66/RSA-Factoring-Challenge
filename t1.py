#!/usr/bin/python3
""" function that return tow boolean
(first boolean True if a bet more than he had left)
or whether b bluffed (second boolean)"""


def bluff(list_tours, a, b):
   
   new_a = a
   new_b = b
   last_idx = len(list_tours) - 1

   if (list_tours is  None or a is None or b is None):
      return None

   if (isinstance(a, int) == False or isinstance(b, int) == False):
      return None

   for i in range (0, last_idx):
      if (isinstance(list_tours[i], int) == False):
         return None

   for a in range (0, (last_idx)):

      if  list_tours[a] >= 0:
         new_a += list_tours[a]
         new_b -= list_tours[a]
      elif list_tours[a] <= 0:

         new_a += list_tours[a]
         new_b -= list_tours[a] 

   if list_tours[last_idx] > 0:

      if list_tours[last_idx] > new_a:
         return True,False

      else:
         return False,False

   elif list_tours[last_idx] < 0:

      if (list_tours[last_idx] * (-1)) > new_b:
         return False,True

      else:
         return False,False
   elif list_tours[last_idx] == 0:
      return False,False


