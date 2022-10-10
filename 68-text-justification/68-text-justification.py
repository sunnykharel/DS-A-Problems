class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        i=0
        res = []
        while i < n:
            start = i
            total_len_words = 0
            total_words = 0
            while i<len(words) and total_len_words+len(words[i])+(total_words+1)-1<=maxWidth:                
                total_len_words+=len(words[i])
                total_words+=1
                i+=1
            number_spaces = 0
            if total_words != 1:
                number_spaces = (maxWidth-total_len_words)//(total_words-1)
            remainder = maxWidth-total_len_words-number_spaces*(total_words-1)
            s=''
            
            if i == len(words):
                remainder = maxWidth
                for j in range(start, i):
                    s+=words[j]
                    s+=' '
                    
                if len(s)> maxWidth:
                    s = s[:maxWidth]
                elif len(s)!=maxWidth:
                    s+=' '*(maxWidth-len(s))
                    
            else:
                for j in range(start, i):
                    s+=words[j]
                    if j !=i-1:
                        s+=' '*number_spaces
                    if j == i-1 and remainder!=0:
                        s+=' '*remainder
                        break
                    if remainder>0:
                        s+=' '
                        remainder-=1
            print(s)
            res.append(s)
                
        return res
            
            # print(total_len_words,total_words-1, i)
            
        