class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        Character[] split = new Character[s.length()];

        for (int i=0; i < s.length(); i++){
            split[i] = (Character) s.charAt(i);
            if ( !map.containsKey(s.charAt(i)))
                map.put(s.charAt(i), 0);
            map.put(s.charAt(i), map.get(s.charAt(i))+1); 
        }
        Comparator<Character> comp = new CustomComparator(map);
        Arrays.sort(split, comp );
        char[] arr = new char[s.length()];
        for (int i = 0; i < s.length(); i++){
            arr[i] = split[i];
        }
        return new String(arr);
        
    }
}

class CustomComparator implements Comparator<Character> 
{ 
    // Used for sorting in ascending order of 
    // roll number
    Map<Character, Integer> map;
    public CustomComparator(Map<Character, Integer> map){
        this.map = map;
    }
    
    public int compare(Character a, Character b) 
    { 
        int diff = this.map.get(b)-this.map.get(a);
        if (diff!=0)
            return diff;
        else
            return a-b;
    } 
}