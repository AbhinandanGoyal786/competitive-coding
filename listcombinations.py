from typing import List

class Solution:
    def getCombinations(self,arr:List[int] , arrnum : int =None):
        '''
        getCombinations function accept n size list and returns all possible combinations of that list.
        arrnum is optional parameter that accept interger value if u send arrnum paramter than it return arrnum sized list all possibile combinations.
        
        '''
        #a=[1,2,1,3,5,1]
        n=len(arr)
        total=2**n
        s=[]
        for i in range(total):
            l1=[]
            for j in range(n):
                if (i>>j & 1):
                    l1.append(arr[j])
            if arrnum is None:    
                s.append(l1)
            elif len(l1)==arrnum:
                s.append(l1)
        return s
print(Solution().getCombinations([1,2,3,4,5],1))
