class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        
        big, small = 0,0
        if len(num1)>len(num2):
            big, small = num1, num2
        else:
            big, small = num2, num1
        
        number = 0
        power_10 = 1
        b = len(big)-1
        s = len(small)-1
        
        while s >= 0:
            place_sum = int(small[s])+int(big[b])+c
            c = 1 if place_sum>9 else 0
            digit = place_sum%10
            number+=power_10*digit
            power_10*=10
            s-=1
            b-=1
        
        if b == -1:
            number += power_10*c
            return "{}".format(number)
        else:
            while b >= 0:
                place_sum = int(big[b])+c
                c = 1 if place_sum>9 else 0
                digit = place_sum%10
                number+=power_10*digit
                power_10*=10
                b-=1
        number +=power_10*c
        return "{}".format(number)
            
            
            