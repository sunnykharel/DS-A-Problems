class Solution {
    public String reverseVowels(String s) {
        int i = 0;
        int j = s.length()-1;
        
        if (s.length() == 0 || s.length()==1) 
            return s;
        
        char[] result = new char[s.length()];
        
        while ( i <= j ){
             if (! isVowel(s.charAt(i)) ){
                result[i] = s.charAt(i); 
                i++;
             }
            if( !isVowel(s.charAt(j))){
                result[j] = s.charAt(j);
                j--;
            }
            else if( isVowel(s.charAt(i)) && isVowel(s.charAt(j)) ){
                result[j] = s.charAt(i);
                result[i] = s.charAt(j);
                i++;j--;
            }
        }
        return new String(result);
        // return "";
    }
    
    public boolean isVowel(char c){
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' ||c=='U';
    }
}