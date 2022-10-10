class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        //we have two options: 
        /*
            
            if equal: we move both
            
            keep pointer at text 1 and move pointer of text 2
            
            keep pointer at text 2 and move pointer of text 1
            
            this is our recursive solution
            
            the subsequence may be distorted
            
            we use the memo 2D array
            
            OPT(i,j) = longest common subsequence for text1[:i] and text2[:j]
            we memoize up on this solution
            by taking a pointer to the other possible solutions that could've happened
            
            OPT(i,j) = 1+opt(i-1,j-1) if a[i] == b[j]
                       else:
                       max ( opt[i-1][j], opt[i][j-1]  ) 
        */
        int[][] opt = new int[text1.length()+1][text2.length()+1];
        
        for (int i = 1; i <=text1.length(); i++){
            for (int j = 1; j<=text2.length(); j++){
                if (text1.charAt(i-1) == text2.charAt(j-1))
                    opt[i][j] = 1+opt[i-1][j-1];
                else
                    opt[i][j] = Math.max( opt[i-1][j], opt[i][j-1] );
            }
        }
        return opt[text1.length()][text2.length()];
    }
}