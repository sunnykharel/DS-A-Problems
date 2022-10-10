class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # return x**n
        
        if(x==-1):
            if n%2==1:
                return -1
            else:
                return 1
        elif n==0 or x==1.0:
            return 1  
        elif(n<0):
            res=1.0
            while(n<0 and 0<abs(res)<2147483648):
                res/=x
                n+=1
            return res
        else:
            res=1.0
            while(n>0 and 0<abs(res)<2147483648):
                res*=x
                n-=1
            return res
        