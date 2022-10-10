class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = (x<0)
        if isNegative:
            x*=-1
        reverse = 0
        while x != 0:
            reverse= reverse*10
            reverse+=x%10
            x/=10
        if ( not(isNegative) and reverse >= 2**31) or (isNegative and reverse>2**31): 
            return 0
        if isNegative:
            return reverse*-1
        return reverse
            
            
        