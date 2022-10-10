class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> conv = new HashMap<>();
        
        conv.put('I',1);
        conv.put('V',5);
        conv.put('X',10);
        conv.put('L',50);
        conv.put('C',100);
        conv.put('D',500);
        conv.put('M',1000);
        //look all cases where I before V/X, uppon hitting these vals only
        //X before L/C
        //C before D/M
        
        int i = 0;
        int total = 0;
        while ( i < s.length() ){
            Character curr = s.charAt(i);
            Character next = 'a';
            if (i+1 < s.length())
                next = s.charAt(i+1);
            if (i == s.length() -1){
                int conv_val = conv.get(curr);
                total+=conv_val;
                i++;
            } 
            else if ( (curr == 'I') && (next == 'V' || next == 'X')){
                total+= conv.get(next)-conv.get(curr);
                i+=2;
            }else if ( (curr == 'X') && (next == 'L' || next == 'C') ){
                total+= conv.get(next)-conv.get(curr);
                i+=2;
            }else if ((curr == 'C') && (next == 'D' || next == 'M')){
                total+= conv.get(next)-conv.get(curr);
                i+=2;
            }else{
                total = total+conv.get(curr);
                i++;
            }
        }
        return total;        
    }
}