class Solution {
    public String sortString(String s) {
        int[] counts = new int[26];
        List<Integer> valids = new ArrayList<>();
        
        for (int i = 0; i < s.length(); i++){
            Character let = s.charAt(i);
            counts[let-'a']++;
        }
        for (int i = 0; i < 26; i++){
            if (counts[i]>0)
                valids.add(i);
        }
        int idx = 0;
        String[] string = new String[s.length()];
        
        while (idx < s.length()){
            for(int i : valids){
                if (counts[i]>0){
                    counts[i]--;
                    string[idx] = ""+(char)('a'+i);
                    idx++;
                }
            }
            for (int i = valids.size()-1; i>=0; i--){
                if (counts[valids.get(i)]>0){
                    counts[valids.get(i)]--;
                    string[idx] = ""+(char)('a'+valids.get(i));
                    idx++;
                } 
            }
        }
        return String.join("", string);
        
        
        
        
        
        
        
   }
}