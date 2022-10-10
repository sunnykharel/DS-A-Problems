class Solution {
    public boolean isRobotBounded(String instructions) {
        Set<String> visited = new HashSet<>();
        
        int[] position = {0,0};
        int direction = 0;
        
        int[][] directions = {
            {0,1},
            {1,0},
            {0,-1},
            {-1,0}
        };
        
        int g_count = 0;
        for (int i = 0; i < instructions.length(); i++ ){
            if (instructions.charAt(i)=='G'){
                g_count++;
            }
        }
        if (g_count==0){
            return true;
        }
        
        for (int j = 0; j <=2*instructions.length(); j++){
            for (int i = 0; i < instructions.length(); i++){
                char inst = instructions.charAt(i);
                if (inst == 'G'){
                    position[0]+=directions[direction][0];
                    position[1]+=directions[direction][1];

                    String pos_str = ""+position[0]+"_"+position[1]+"_"+i;
                    if (visited.contains(pos_str)){
                        // System.out.println(pos_str);
                        // System.out.println(visited);
                        return true;
                    }
                    visited.add(pos_str);
                }else if (inst == 'L'){
                    direction = (direction-1+4)%4;
                    // System.out.println(direction);
                } else {
                    direction = (direction+1)%4;
                }
            }
        }
        return false;
        
    }
}