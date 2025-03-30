'''
The values in the list represent the cost to switch
goal is to get to smallest index in list using lowest cost
person #3 has the lowest cost
how does the person behind me swap for free?

  <--  0 1 2 3 4 5  n
in =  [5,3,4,1,3,2]          
           x       
pay person #3 $1 but ask person #2 to swap, that will put me at index 2 with a cost of $1

[5,3,4,1,3,2] #0
[5,3,3,3,3,3] #1
[5,3,4,1,3,2] #2
[5,3,4,1,1,1] #3
[5,3,4,1,3,1] #4
[5,3,4,1,3,2] #5
[5,3,3,1,1,1] result is a representation of what it would cost to reach index

                            swap cost pay
                             0    5    
                             1    3    
                             2    4    1  if I'm at this index my cost is $1
                             3    1    1  i want to be here because it costs the least
                             4    3    
                             5    2    
                             6    0
out = [5,3,3,1,1,1]
'''

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        # res = list(cost)
        # paid = cost[i]
        # for i, val in cost:
        #     current = res[i]
        #     if res[i+1] > current:
        for i in range(1, len(cost)):
            cost[i] = min(cost[i-1], cost[i])
        return cost
                
        # 1 - set the lowest price --->
        # i = 0, every increasing index will contain the smallest value - original or paid
        # i = 1, ''

        
        
        