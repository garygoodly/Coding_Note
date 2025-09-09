'''
This problem can be regard as "Determine whether there's a loop in linked list".
Therefor, fast, slow pointer can be used to solve this.
'''

class Solution:
   def isHappy(self, n: int) -> bool:        
       slow = n
       fast = n
       while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
           slow = self.get_sum(slow)
           fast = self.get_sum(self.get_sum(fast))
           if slow == fast:
               return False
       return True
   def get_sum(self,n: int) -> int: 
       new_num = 0
       while n:
           n, r = divmod(n, 10)
           new_num += r ** 2
       return new_num