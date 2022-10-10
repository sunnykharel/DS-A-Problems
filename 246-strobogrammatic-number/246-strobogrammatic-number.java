class Solution {
    public boolean isStrobogrammatic(String num) {
        //ie it only has numbers that are upside downable
        String upside_down = "";
        Set<Character> non_upside = new HashSet<>( Arrays.asList('2','3','4','5','7') );
        
        for (int i = 0; i < num.length(); i++){
            if (non_upside.contains(num.charAt(i))){
                return false;
            }else{
                if (num.charAt(i)=='6')
                    upside_down='9'+upside_down;
                else if(num.charAt(i)=='9')
                    upside_down='6'+upside_down;
                else
                    upside_down=num.charAt(i)+upside_down;
            }
        }
        
        return num.equals(upside_down);
    }
}