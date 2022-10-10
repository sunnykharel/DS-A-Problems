class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        //determine whether the last character can be a two bit character
        //if so then false
        //so we take two for the last two and try to decode
        /*
            [1,0,0]
            we have so solve recursively
            
            three combos:
                10 or 11 for two bit pairs, or 0 for one bit
                we try decoding as all three and or them
        
        */
        
        if(bits.length == 0)
            return false;
        
        if (bits.length == 1)
            return true;

        if (bits[bits.length-2] == 0 )
            return true;
    
        if (bits.length == 2 &&  bits[0]==1)
            return false;

        if (bits[bits.length-2] == 1 )
            return !recursion(bits, bits.length-3);
        return true;
         
    }
    
    public boolean recursion(int[] bits, int depth){
        if (depth < 0){
            return true;
        }
        if (depth == 0)
            return bits[0]==0;
        else{
            boolean two = false;
            boolean one = false;
            if ( bits[depth-1] == 1 )
                two = recursion(bits, depth-2);
            if ( bits[depth] == 0 )
                one = recursion(bits, depth-1);
            return two || one;
        }
        
        
        
    }
}